import ipywidgets as w
from ._definer import Definer
from ...data import Word

class Glossary(w.VBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.IGNORE_EVENTS = False
        self.LOADED_GLOSSARY = []
        self._grid = w.GridspecLayout(10, 4)

        self._btn_new = w.Button(
            description = "New",
            layout = w.Layout(width = "auto"))

        self._btn_delete = w.Button(
            description = "Delete", 
            layout = w.Layout(width = "auto"))

        self._word_display = w.Box(layout = w.Layout(height = "auto", width = "auto"))
        self._word_list = w.Select(layout = w.Layout(height = "auto", width = "auto"))

        self._grid[0, 0] = self._btn_new
        self._grid[0, 1] = self._btn_delete
        self._grid[1:, :2] = self._word_list
        self._grid[0:, 2:] = self._word_display

        self._definer = Definer()
        self.children = self.widgets

        self._btn_new.on_click(self.handle_new)
        self._definer.on_save(self.handle_save_word)
        self._definer.on_cancel(self.handle_cancel)
        self._word_list.observe(self.handle_select_word, "value")

    @property
    def widgets(self):
        return [
            self._grid
        ]

    def handle_new(self, _):
        self._word_display.children = [self._definer]
        self._definer.new_word()

    def handle_cancel(self):
        self._word_list.index = None
        self._word_display.children = []

    def handle_save_word(self, word, original = None):
        if original:
            self.LOADED_GLOSSARY.remove(original)
        self._word_display.children = []
        self.IGNORE_EVENTS = True
        self.LOADED_GLOSSARY.append(word)
        self.LOADED_GLOSSARY = sorted(self.LOADED_GLOSSARY)
        self._word_list.options = [w.dictionary_form for w in self.LOADED_GLOSSARY]
        self._word_list.index = None
        self.IGNORE_EVENTS = False

        print(self.save_data())

    def handle_select_word(self, _):
        if self._word_list.index is not None and not self.IGNORE_EVENTS:
            self._definer.open_word(self.LOADED_GLOSSARY[self._word_list.index])
            self._word_display.children = [self._definer]

    def save_data(self):
        _verbs = [w for w in self.LOADED_GLOSSARY if w.type == Word.Type.VERB]
        _nouns = [w for w in self.LOADED_GLOSSARY if w.type == Word.Type.NOUN]

        return {
            "nouns": [n.save_data() for n in _nouns],
            "verbs": [v.save_data() for v in _verbs]
        }
