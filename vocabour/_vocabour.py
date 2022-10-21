import json
from . import vdata
import ipywidgets as w
from .globals import DATA_DIRECTORY, DATA_FULL_PATH
from ._drill_definitions import DrillDefinitions
from .sections import Glossary

class Vocabour(w.VBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._glossary = Glossary()
        self._drill_defs = DrillDefinitions()

        # options
        self._btn_glossary = w.Button(description = "Glossary")
        # drills
        self._btn_drill_defs = w.Button(description = "Defintions")

        if not DATA_DIRECTORY.exists():
            DATA_DIRECTORY.mkdir()

        self._accordian = w.Accordion()

        self._accordian.children = self.menu
        self._accordian.set_title(0, "Settings")
        self._accordian.set_title(1, "Drills")

        self.children = [self._accordian]

        self._btn_glossary.on_click(self.handle_glossary)
        self._glossary.on_exit(self.handle_glossary_exit)
        self._drill_defs.menu_callback = self.handle_menu_callback
        self._btn_drill_defs.on_click(self.handle_open_drill_defs)

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

    def handle_glossary(self, _):
        self._glossary.load(self._get_glossary())
        self.children = [self._glossary]

    def handle_menu_callback(self, _ = None):
        self.children = [self._accordian]

    def handle_glossary_exit(self, glossary):
        _save = self._save_glossary(glossary.LOADED_GLOSSARY)
        with open(DATA_FULL_PATH, "w") as file:
            file.write(json.dumps(_save))
        self.handle_menu_callback()

    def handle_open_drill_defs(self, _):
        _gloss = self._get_glossary()
        self._drill_defs.load_data({w.dictionary_form: w.definition for w in _gloss})
        self.children = [self._drill_defs]

    def _get_glossary(self):
        if DATA_FULL_PATH.exists():
            _glossary = []
            with open(DATA_FULL_PATH, "r") as file:
                _data = json.loads(file.read())
                for n in _data.get("nouns", []):
                    _glossary.append(vdata.Noun.from_data(n))
                for v in _data.get("verbs", []):
                    _glossary.append(vdata.Verb.from_data(v))
            return _glossary
        return None

    def _save_glossary(self, glossary):
        _verbs = [w for w in glossary if w.type == vdata.Word.Type.VERB]
        _nouns = [w for w in glossary if w.type == vdata.Word.Type.NOUN]

        return {
            "nouns": [n.save_data() for n in _nouns],
            "verbs": [v.save_data() for v in _verbs]
        }

    # def load_vocab(self, path, batch = False):
    #     path_obj = pathlib.Path(path)

    #     if path_obj.is_dir():
    #         if batch:
    #             for x in path_obj.iterdir():
    #                 with open(x, "rb") as file:
    #                     self.VOCAB[x.name.replace(".json", "")] = json.load(file)
    #         else:
    #             raise IsADirectoryError(f"{path} is a directory, but batch is set to False")

    #     self._fld_topics.options = ["*", *[k for k in self.VOCAB.keys()]]
