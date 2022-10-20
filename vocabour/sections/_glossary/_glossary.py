import ipywidgets as w
from ._definer import Definer

class Glossary(w.VBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._grid = w.GridspecLayout(10, 4)

        self._btn_new = w.Button(
            description = "New",
            layout = w.Layout(width = "auto"))

        self._btn_delete = w.Button(
            description = "Delete", 
            layout = w.Layout(width = "auto"))

        self._word_display = w.Box(
            layout = w.Layout(height = "auto", width = "auto"))
        self._word_list = w.SelectMultiple(
            layout = w.Layout(height = "auto", width = "auto"))

        self._grid[0, 0] = self._btn_new
        self._grid[0, 1] = self._btn_delete
        self._grid[1:, :2] = self._word_list
        self._grid[0:, 2:] = self._word_display

        self._definer = Definer()
        self.children = self.widgets

        self._btn_new.on_click(self.handle_new)
        self._definer.on_save(self.handle_save_word)

    @property
    def widgets(self):
        return [
            self._grid
        ]

    def handle_new(self, _):
        self._word_display.children = [self._definer]

    def handle_save_word(self, word):
        print(word)
