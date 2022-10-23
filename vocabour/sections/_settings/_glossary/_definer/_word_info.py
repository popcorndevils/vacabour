import ipywidgets as w
from .....types import Word

class WordInfo:
    def __init__(self):
        # normal settings
        self.fld_dictionary = w.Text(
            placeholder = "ex: работать",
            layout = w.Layout(width = "auto"))
        self.fld_definition = w.Text(
            placeholder = "ex: to work",
            layout = w.Layout(width = "auto"))

        # advanced settings
        self._fld_sentence = w.Text(layout = w.Layout(width = "auto"))
        self._fld_attempts = w.IntText(layout = w.Layout(width = "auto"))
        self._fld_correct = w.IntText(layout = w.Layout(width = "auto"))
        self._fld_tags = w.Textarea(
            placeholder = "TAGs",
            layout = w.Layout(width = "auto"))

        # advanced settings
        self._grid_advanced = w.GridspecLayout(3, 4)

        self._grid_advanced[0, 0] = w.Label("Sentence")
        self._grid_advanced[0, 1:] = self._fld_sentence
        self._grid_advanced[1, 0] = w.Label("Attempts")
        self._grid_advanced[1, 1:] = self._fld_attempts
        self._grid_advanced[2, 0] = w.Label("Correct")
        self._grid_advanced[2, 1:] = self._fld_correct

        self.advanced_settings = w.Accordion(
            children = self.special,
            selected_index = None,
            layout = w.Layout(width = "auto"))

        self.advanced_settings.set_title(0, "Advanced")

    @property
    def special(self):
        return [w.VBox([
            self._grid_advanced,
            self._fld_tags
        ])]

    @property
    def dictionary(self):
        return self.fld_dictionary.value.lower()

    @dictionary.setter
    def dictionary(self, value):
        if isinstance(value, str):
            self.fld_dictionary.value = value.lower()
        else:
            self.fld_dictionary.value = ""

    @property
    def definition(self):
        return self.fld_definition.value

    @definition.setter
    def definition(self, value):
        if isinstance(value, str):
            self.fld_definition.value = value
        else:
            self.fld_definition.value = ""

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
    def attempts(self):
        return self._fld_attempts.value

    @attempts.setter
    def attempts(self, value):
        if value is not None:
            self._fld_attempts.value = value
        else:
            self._fld_attempts.value = 0

    @property
    def correct(self):
        return self._fld_correct.value

    @correct.setter
    def correct(self, value):
        if isinstance(value, int):
            self._fld_correct.value = value
        else:
            self._fld_correct.value = 0

    @property
    def tags(self):
        return [t.strip() for t in self._fld_tags.value.lower().replace("\n", ",").split(",")]

    @tags.setter
    def tags(self, value):
        if isinstance(value, int):
            self._fld_tags.value = ", ".join(value)

    def open_word(self, word: Word):
        self.dictionary = word.dictionary_form
        self.definition = word.definition
        self.sentence_form = word.sentence_form
        self.attempts = word.attempts
        self.correct = word.correct
        self.tags = word.tags

    def save_data(self):
        _out = Word()
        _out.dictionary_form = self.dictionary
        _out.definition = self.definition
        _out.sentence_form = self.sentence_form
        _out.attempts = self.attempts
        _out.correct = self.correct
        _out.tags = self.tags
        return _out.save_data()

    def observe_dictionary(self, *args, **kwargs):
        self.fld_dictionary.observe(*args, **kwargs)

    def reset(self):
        self.dictionary = ""
        self.definition = ""
        self.sentence_form = ""
        self.attempts = 0
        self.correct = 0
        self.tags = ""
        self.advanced_settings.selected_index = None
