import ipywidgets as w
from ._def_verb import DefVerb
from ._def_pronoun import DefPronoun
from ._def_menu import DefMenu
from .... import types

class DefManager(DefMenu):
    def __init__(self, *args, **kwargs):
        super().__init__(1, 1, *args, **kwargs)
        self._container = w.Box()

        self.TYPES = {
            "VERB": DefVerb(),
            "PRONOUN": DefPronoun(),
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
        self.content[0, 0] = self.TYPES[self._select.value]

    def open_word(self, word):
        if isinstance(word, types.Word):
            _definer_type = None

            if isinstance(word, types.Verb):
                _definer_type = "VERB"
            if isinstance(word, types.Pronoun):
                _definer_type = "PRONOUN"

            if _definer_type is not None:
                self._select.value = _definer_type
                _definer = self.TYPES[_definer_type]
                self._select.disabled = True
                self._EDIT_WORD = word
                self.content[0, 0] = _definer
                _definer.open_word(word)

    def reset(self):
        self._EDIT_WORD = None
        self._select.disabled = False
