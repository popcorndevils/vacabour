import ipywidgets as w
from ._def_menu import DefMenu
from ._word_info import WordInfo
from ....types import Pronoun

class DefPronoun(DefMenu):
    def __init__(self, *args, **kwargs):
        super().__init__(6, 4, *args, **kwargs)
        self._btn_save = w.Button(description = "Save", layout = w.Layout(width = "auto"))
        self._btn_cancel = w.Button(description = "Cancel", layout = w.Layout(width = "auto"))

        self._wordinfo = WordInfo()

        self._fld_genative = w.Text(layout = w.Layout(width = "auto"))
        self._fld_dative = w.Text(layout = w.Layout(width = "auto"))
        self._fld_accusative = w.Text(layout = w.Layout(width = "auto"))
        self._fld_instrumental = w.Text(layout = w.Layout(width = "auto"))
        self._fld_prepositional = w.Text(layout = w.Layout(width = "auto"))

        self.header = self._wordinfo

        self.content[0, 0] = w.Label("Genative")
        self.content[0, 1:] = self._fld_genative
        self.content[1, 0] = w.Label("Accusative")
        self.content[1, 1:] = self._fld_accusative
        self.content[2, 0] = w.Label("Dative")
        self.content[2, 1:] = self._fld_dative
        self.content[3, 0] = w.Label("Prepositional")
        self.content[3, 1:] = self._fld_prepositional
        self.content[4, 0] = w.Label("Instrumental")
        self.content[4, 1:] = self._fld_instrumental

        self.content[-1, :2] = self._btn_save
        self.content[-1, 2:] = self._btn_cancel

        self._btn_save.on_click(self.handle_save)
        self._btn_cancel.on_click(lambda _: self.cancel_word())

        self.reset()

    def open_word(self, word: Pronoun):
        super().open_word(word)
        self._wordinfo.open_word(word)
        self._fld_genative.value = word.genative
        self._fld_dative.value = word.dative
        self._fld_accusative.value = word.accusative
        self._fld_instrumental.value = word.instrumental
        self._fld_prepositional.value = word.prepositional

    def handle_save(self, _):
        _out = Pronoun.from_data(self._wordinfo.save_data())

        _out.genative = self._fld_genative.value.lower()
        _out.dative = self._fld_dative.value.lower()
        _out.accusative = self._fld_accusative.value.lower()
        _out.instrumental = self._fld_instrumental.value.lower()
        _out.prepositional = self._fld_prepositional.value.lower()

        self.save_word(_out)

    def reset(self):
        self._wordinfo.reset()
        self._fld_genative.value = ""
        self._fld_dative.value = ""
        self._fld_accusative.value = ""
        self._fld_instrumental.value = ""
        self._fld_prepositional.value = ""
