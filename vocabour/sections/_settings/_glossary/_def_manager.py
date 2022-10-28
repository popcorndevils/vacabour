import ipywidgets as w
from . import _definer as define
from ._def_menu import DefMenu
from vocabour import types

class DefManager(DefMenu):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.TYPES = {
            "ADJECTIVE": define.DefAdjective(),
            "ADVERB": define.DefAdverb(),
            "NOUN": define.DefNoun(),
            "PHRASE": define.DefPhrase(),
            "PRONOUN": define.DefPronoun(),
            "VERB": define.DefVerb(),
            "GENERIC": define.DefGeneric(),
        }

        self._select = w.Dropdown()
        self._select.observe(self.handle_select, "value")

        self._select.options = [k for k in self.TYPES.keys()]

        for d in self.TYPES.values():
            d.on_save_word(lambda w, _: self.save_word(w))
            d.on_cancel_word(lambda: self.cancel_word())

        self.header = self._select

    def new_word(self):
        for t in self.TYPES.values():
            t.new_word()
        super().new_word()

    def handle_select(self, _):
        self.content = self.TYPES[self._select.value]

    def open_word(self, word):
        if isinstance(word, types.Word):
            _definer_type = None

            if isinstance(word, types.Adjective):
                _definer_type = "ADJECTIVE"
            if isinstance(word, types.Adverb):
                _definer_type = "ADVERB"
            if isinstance(word, types.Generic):
                _definer_type = "GENERIC"
            if isinstance(word, types.Noun):
                _definer_type = "NOUN"
            if isinstance(word, types.Phrase):
                _definer_type = "PHRASE"
            if isinstance(word, types.Pronoun):
                _definer_type = "PRONOUN"
            if isinstance(word, types.Verb):
                _definer_type = "VERB"

            if _definer_type is not None:
                self._select.value = _definer_type
                _definer = self.TYPES[_definer_type]
                self._select.disabled = True
                self._EDIT_WORD = word
                self.content = _definer
                _definer.open_word(word)

    def reset(self):
        self._EDIT_WORD = None
        self._select.disabled = False
