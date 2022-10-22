import ipywidgets as w
from ._def_menu import DefMenu
from ....types import Pronoun

class DefPronoun(DefMenu):
    def __init__(self, *args, **kwargs):
        super().__init__(13, 2, *args, **kwargs)
        self._btn_save = w.Button(
            description = "Save",
            layout = w.Layout(width = "auto"))
        self._btn_cancel = w.Button(
            description = "Cancel",
            layout = w.Layout(width = "auto"))

        self._fld_dictionary = w.Text(layout = w.Layout(width = "auto"))
        self._fld_definition = w.Text(layout = w.Layout(width = "auto"))
        self._fld_genative = w.Text(layout = w.Layout(width = "auto"))
        self._fld_dative = w.Text(layout = w.Layout(width = "auto"))
        self._fld_accusative = w.Text(layout = w.Layout(width = "auto"))
        self._fld_instrumental = w.Text(layout = w.Layout(width = "auto"))
        self._fld_prepositional = w.Text(layout = w.Layout(width = "auto"))

        self._fld_tags = w.Textarea(
            placeholder = "TAGs",
            layout = w.Layout(width = "auto", height = "100%"))

        self.content[0, 0] = w.Label("Dictionary")
        self.content[1, 0] = w.Label("Definition")
        self.content[3, 0] = w.Label("Genative")
        self.content[2, 0] = w.Label("Dative")
        self.content[4, 0] = w.Label("Accusative")
        self.content[5, 0] = w.Label("Instrumental")
        self.content[6, 0] = w.Label("Prepositional")

        self.content[0, 1] = self._fld_dictionary
        self.content[1, 1] = self._fld_definition
        self.content[2, 1] = self._fld_genative
        self.content[3, 1] = self._fld_dative
        self.content[4, 1] = self._fld_accusative
        self.content[5, 1] = self._fld_instrumental
        self.content[6, 1] = self._fld_prepositional
        self.content[7:-1, 0:] = self._fld_tags
        self.content[-1, 0] = self._btn_save
        self.content[-1, 1] = self._btn_cancel

        self._btn_save.on_click(self.handle_save)
        self._btn_cancel.on_click(lambda: self.handle_cancel())

        self.reset()

    def open_word(self, word: Pronoun):
        super().open_word(word)
        self._fld_dictionary.value = word.dictionary_form
        self._fld_definition.value = word.definition
        self._fld_genative.value = word.genative
        self._fld_dative.value = word.dative
        self._fld_accusative.value = word.accusative
        self._fld_instrumental.value = word.instrumental
        self._fld_prepositional.value = word.prepositional
        self._fld_tags.value = ", ".join(word.tags)

    def handle_save(self, _):
        _out = Pronoun()
        _base = self._fld_dictionary.value.lower()

        _out.dictionary_form = _base
        _out.definition = self._fld_definition.value.lower()
        _out.genative = self._fld_genative.value.lower()
        _out.dative = self._fld_dative.value.lower()
        _out.accusative = self._fld_accusative.value.lower()
        _out.instrumental = self._fld_instrumental.value.lower()
        _out.prepositional = self._fld_prepositional.value.lower()
        _out.tags = [t.strip() for t in self._fld_tags.value.lower().replace("\n", ",").split(",")]

        self.save_word(_out)

    def reset(self):
        self._fld_dictionary.value = ""
        self._fld_definition.value = ""
        self._fld_genative.value = ""
        self._fld_dative.value = ""
        self._fld_accusative.value = ""
        self._fld_instrumental.value = ""
        self._fld_prepositional.value = ""
        self._fld_tags.value = ""
