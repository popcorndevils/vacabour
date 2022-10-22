import ipywidgets as w
from ....types import Word

class WordInfo(w.VBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._fld_dictionary = w.Text(layout = w.Layout(width = "auto"))
        self._fld_definition = w.Text(layout = w.Layout(width = "auto"))

        self._grid = w.GridspecLayout(2, 2)
        self._grid[0, 0] = w.Label("Dictionary")
        self._grid[1, 0] = w.Label("Definition")
        self._grid[0, 1] = self._fld_dictionary
        self._grid[1, 1] = self._fld_definition

        self._fld_tags = w.Textarea(
            placeholder = "TAGs",
            layout = w.Layout(width = "auto", height = "auto"))

        self._sec_special = w.Accordion(children = self.special, selected_index = None)
        self._sec_special.set_title(0, "Advanced")

        self.children = [self._grid, self._sec_special]

    @property
    def special(self):
        return [
            self._fld_tags
        ]

    @property
    def dictionary(self):
        return self._fld_dictionary.value.lower()

    @dictionary.setter
    def dictionary(self, value):
        self._fld_dictionary.value = value.lower()

    @property
    def definition(self):
        return self._fld_definition.value

    @definition.setter
    def definition(self, value):
        self._fld_definition.value = value

    @property
    def tags(self):
        return [t.strip() for t in self._fld_tags.value.lower().replace("\n", ",").split(",")]

    @tags.setter
    def tags(self, value):
        self._fld_tags.value = ", ".join(value)

    def open_word(self, word: Word):
        self.dictionary = word.dictionary_form
        self.definition = word.definition
        self.tags = word.tags

    def save_data(self):
        _out = Word()
        _out.dictionary_form = self.dictionary
        _out.definition = self.definition
        _out.tags = self.tags
        return _out.save_data()

    def observe_dictionary(self, *args, **kwargs):
        self._fld_dictionary.observe(*args, **kwargs)

    def reset(self):
        self.dictionary = ""
        self.definition = ""
        self.tags = ""
        self._sec_special.selected_index = None
