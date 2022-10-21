import ipywidgets as w
from ._define_verb import DefineVerb
from ...data import Verb

class Definer(w.VBox):
    def __init__(self):
        super().__init__()
        self._REGISTERED_SAVE_WORD = []
        self._REGISTERED_CANCEL = []
        self._EDIT_WORD = None
        self._container = w.Box()

        self._def_verb = DefineVerb()

        self.TYPES = {
            "VERB": self._def_verb
        }

        self._select = w.Dropdown()
        self._select.observe(self.handle_select, "value")

        self.children = self.widgets
        self._select.options = [k for k in self.TYPES.keys()]

        self._def_verb.on_save(self.handle_receive_word)
        self._def_verb.on_cancel(self.handle_cancel)

    @property
    def widgets(self):
        return [
            self._select,
            self._container
        ]

    def on_save(self, func):
        self._REGISTERED_SAVE_WORD.append(func)

    def on_cancel(self, func):
        self._REGISTERED_CANCEL.append(func)

    def new_word(self):
        self._EDIT_WORD = None
        for t in self.TYPES.values():
            t.new_word()

    def handle_select(self, _):
        self._container.children = [self.TYPES[self._select.value]]

    def handle_cancel(self):
        self._EDIT_WORD = None
        for f in self._REGISTERED_CANCEL:
            f()

    def handle_receive_word(self, word):
        for f in self._REGISTERED_SAVE_WORD:
            if self._EDIT_WORD:
                f(word, self._EDIT_WORD)
            else:
                f(word)
        self._EDIT_WORD = None

    def open_word(self, word):
        self._EDIT_WORD = word
        if isinstance(word, Verb):
            self._select.value = "VERB"
            self._def_verb.open_word(word)
