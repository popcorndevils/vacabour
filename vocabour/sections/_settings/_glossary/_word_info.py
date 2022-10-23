from logging import PlaceHolder
import ipywidgets as w
from ....types import Word

class WordInfo(w.VBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # normal settings
        self._fld_dictionary = w.Text(placeholder = "ex: работать")
        self._fld_definition = w.Text()
        # advanced settings
        self._fld_sentence = w.Text()
        self._fld_tags = w.Textarea(
            placeholder = "TAGs",
            layout = w.Layout(width = "auto"))
        # grids
        self._grid = w.GridspecLayout(2, 4)
        self._grid_advanced = w.GridspecLayout(1, 4)
        # normal grid layout
        self._grid[0, 0] = w.Label("Dictionary")
        self._grid[1, 0] = w.Label("Definition")
        self._grid[0, 1:] = self._fld_dictionary
        self._grid[1, 1:] = self._fld_definition
        # advanced grid layout
        self._grid_advanced[0, 0] = w.Label("Sentence")
        self._grid_advanced[0, 1:] = self._fld_sentence

        self._sec_advanced = w.Accordion(children = self.special, selected_index = None, layout = w.Layout(width = "auto"))
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
        if isinstance(value, str):
            self._fld_dictionary.value = value.lower()
        else:
            self._fld_dictionary.value = ""

    @property
    def definition(self):
        return self._fld_definition.value

    @definition.setter
    def definition(self, value):
        if isinstance(value, str):
            self._fld_definition.value = value
        else:
            self._fld_definition.value = ""

    @property
    def sentence_form(self):
        return self._fld_sentence.value.lower()

    @sentence_form.setter
    def sentence_form(self, value):
        if isinstance(value, str):
            self._fld_sentence.value = value
        else:
            self._fld_sentence.value = ""

    @property
    def tags(self):
        return [t.strip() for t in self._fld_tags.value.lower().replace("\n", ",").split(",")]

    @tags.setter
    def tags(self, value):
        if value is not None:
            self._fld_tags.value = ", ".join(value)

    def open_word(self, word: Word):
        self.dictionary = word.dictionary_form
        self.definition = word.definition
        self.sentence_form = word.sentence_form
        self.tags = word.tags

    def save_data(self):
        _out = Word()
        _out.dictionary_form = self.dictionary
        _out.definition = self.definition
        _out.tags = self.tags
        _out.sentence_form = self.sentence_form
        return _out.save_data()

    def observe_dictionary(self, *args, **kwargs):
        self._fld_dictionary.observe(*args, **kwargs)

    def reset(self):
        self.dictionary = ""
        self.definition = ""
        self.tags = ""
        self.sentence_form = ""
        self._sec_advanced.selected_index = None
