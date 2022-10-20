import ipywidgets as w
from ._define_verb import DefineVerb

class Definer(w.VBox):
    def __init__(self):
        super().__init__()
        self._REGISTERED_SAVE_WORD = []
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

    @property
    def widgets(self):
        return [
            self._select,
            self._container
        ]

    def on_save(self, func):
        self._REGISTERED_SAVE_WORD.append(func)

    def handle_select(self, _):
        self._container.children = [self.TYPES[self._select.value]]

    def handle_receive_word(self, word):
        if len(self._REGISTERED_SAVE_WORD) > 0:
            for f in self._REGISTERED_SAVE_WORD:
                f(word)
