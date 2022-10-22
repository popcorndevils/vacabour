import ipywidgets as w
from ._def_verb import DefVerb
from ._def_menu import DefMenu
from .... import types

class DefManager(DefMenu):
    def __init__(self, *args, **kwargs):
        super().__init__(1, 1, *args, **kwargs)
        self._container = w.Box()

        self._def_verb = DefVerb()

        self.TYPES = {
            "VERB": self._def_verb
        }

        self._select = w.Dropdown()
        self._select.observe(self.handle_select, "value")

        self._select.options = [k for k in self.TYPES.keys()]

        self._def_verb.on_save_word(self.handle_receive_word)
        self._def_verb.on_cancel_word(self.handle_cancel)

        self.header = self._select

    def new_word(self):
        for t in self.TYPES.values():
            t.new_word()
        super().new_word()
        self._unlock()

    def handle_select(self, _):
        self.content[0, 0] = self.TYPES[self._select.value]

    def handle_cancel(self):
        self._unlock()
        super().cancel_word()

    def handle_receive_word(self, word, _):
        super().save_word(word)
        self._unlock()

    def open_word(self, word):
        if isinstance(word, types.Word):
            self._select.disabled = True
            self._EDIT_WORD = word
            if isinstance(word, types.Verb):
                self._select.value = "VERB"
                self.content[0, 0] = self.TYPES[self._select.value]
                self._def_verb.open_word(word)

    def _unlock(self):
        self._EDIT_WORD = None
        self._select.disabled = False
