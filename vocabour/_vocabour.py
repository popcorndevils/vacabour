import json
import ipywidgets as w
from . import types
from .sections import drills
from .sections import Glossary
from .globals import DATA_DIRECTORY, DATA_FULL_PATH

class Vocabour(w.VBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._glossary = Glossary()
        self._drills = drills.GameBrowser()

        # sections
        self._btn_glossary = w.Button(description = "Glossary")
        self._btn_drill_defs = w.Button(description = "Drills")

        if not DATA_DIRECTORY.exists():
            DATA_DIRECTORY.mkdir()

        self._accordian = w.Accordion()

        self._accordian.children = self.menu
        self._accordian.set_title(0, "Settings")
        self._accordian.set_title(1, "Drills")

        self.children = [self._accordian]

        self._btn_glossary.on_click(self.handle_open_glossary)
        self._btn_drill_defs.on_click(self.handle_open_drill_defs)

        self._glossary.on_exit(self.handle_section_exit)
        self._drills.on_exit(self.handle_section_exit)
        self._glossary.on_save(self.handle_save_glossary)
        self._drills.on_save(self.handle_save_glossary)

    @property
    def menu(self):
        return [
            w.VBox([
                self._btn_glossary
            ]),
            w.VBox([
                self._btn_drill_defs
            ]),
        ]

    def handle_open_glossary(self, _):
        self._glossary.load(self._get_glossary())
        self.children = [self._glossary]

    def handle_drill_exit(self, drill):
        _save = self._save_glossary(drill.LOADED_GLOSSARY)
        with open(DATA_FULL_PATH, "w") as file:
            file.write(json.dumps(_save))
        self._reset()

    def handle_save_glossary(self, glossary):
        _save = self._save_glossary(glossary.LOADED_GLOSSARY)
        with open(DATA_FULL_PATH, "w") as file:
            file.write(json.dumps(_save))

    def handle_section_exit(self, sender):
        self._reset()

    def handle_open_drill_defs(self, _):
        self._drills.load(self._get_glossary())
        self.children = [self._drills]

    def _reset(self):
        self.children = [self._accordian]

    def _get_glossary(self):
        if DATA_FULL_PATH.exists():
            _glossary = []
            with open(DATA_FULL_PATH, "r") as file:
                _data = json.loads(file.read())
                for v in _data.get("adjectives", []):
                    _glossary.append(types.Adjective.from_data(v))
                for v in _data.get("adverbs", []):
                    _glossary.append(types.Adverb.from_data(v))
                for n in _data.get("generic", []):
                    _glossary.append(types.Generic.from_data(n))
                for n in _data.get("nouns", []):
                    _glossary.append(types.Noun.from_data(n))
                for v in _data.get("phrases", []):
                    _glossary.append(types.Phrase.from_data(v))
                for v in _data.get("pronouns", []):
                    _glossary.append(types.Pronoun.from_data(v))
                for v in _data.get("verbs", []):
                    _glossary.append(types.Verb.from_data(v))
            return _glossary
        return None

    def _save_glossary(self, glossary):
        return {
            "adjectives": [w.save_data() for w in glossary if isinstance(w, types.Adjective)],
            "adverbs": [w.save_data() for w in glossary if isinstance(w, types.Adverb)],
            "generic": [w.save_data() for w in glossary if isinstance(w, types.Generic)],
            "nouns": [w.save_data() for w in glossary if isinstance(w, types.Noun)],
            "phrases": [w.save_data() for w in glossary if isinstance(w, types.Phrase)],
            "pronouns": [w.save_data() for w in glossary if isinstance(w, types.Pronoun)],
            "verbs": [w.save_data() for w in glossary if isinstance(w, types.Verb)],
        }
