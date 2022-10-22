import ipywidgets as w
from ....types import Word

class WordInfo(w.VBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # normal settings
        self._fld_dictionary = w.Text(layout = w.Layout(width = "auto"))
        self._fld_definition = w.Text(layout = w.Layout(width = "auto"))
        # advanced settings
        self._fld_sentence = w.Text()
        self._fld_tags = w.Textarea(
            placeholder = "TAGs",
            layout = w.Layout(width = "auto", height = "auto"))
        # grids
        self._grid = w.GridspecLayout(2, 2)
        self._grid_advanced = w.GridspecLayout(1, 2)
        # normal grid layout
        self._grid[0, 0] = w.Label("Dictionary")
        self._grid[1, 0] = w.Label("Definition")
        self._grid[0, 1] = self._fld_dictionary
        self._grid[1, 1] = self._fld_definition
        # advanced grid layout
        self._grid_advanced[0, 0] = w.Label("Sentence")
        self._grid_advanced[0, 1] = self._fld_sentence

        self._sec_advanced = w.Accordion(children = self.special, selected_index = None)
        self._sec_advanced.set_title(0, "Advanced")

        self.children = [self._grid, self._sec_advanced]

    @property
    def special(self):
        return [w.VBox([
            self._grid_advanced,
            self._fld_tags
        ])]

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
        self._fld_sentence.value = word.sentence_form
        self.tags = word.tags

    def save_data(self):
        _out = Word()
        _out.dictionary_form = self.dictionary
        _out.definition = self.definition
        _out.tags = self.tags
        _out.sentence_form = self._fld_sentence.value
        return _out.save_data()

    def observe_dictionary(self, *args, **kwargs):
        self._fld_dictionary.observe(*args, **kwargs)

    def reset(self):
        self.dictionary = ""
        self.definition = ""
        self.tags = ""
        self._fld_sentence.value = ""
        self._sec_advanced.selected_index = None
