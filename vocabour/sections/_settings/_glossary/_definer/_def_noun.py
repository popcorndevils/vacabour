import ipywidgets as w
from ._base_definer import BaseDefiner
from .....types import Noun
from .....grammar import Nominative
from .....grammar._cyrilic import Genders

class DefNoun(BaseDefiner):
    def __init__(self, *args, **kwargs):
        super().__init__(Noun, *args, **kwargs)
        self.GENDERS = [
            Genders.MASCULINE,
            Genders.FEMININE,
            Genders.NEUTER,
        ]

        self._grid = w.GridspecLayout(5, 4)
        self._grid_g = w.GridspecLayout(1, 4)

        self._gender = w.Dropdown(options = [g for g in self.GENDERS])

        self._fld_sing_nom = w.Text(layout = w.Layout(width = "auto"), disabled = True)
        self._fld_sing_gen = w.Text(layout = w.Layout(width = "auto"))
        self._fld_sing_dat = w.Text(layout = w.Layout(width = "auto"))
        self._fld_sing_acc = w.Text(layout = w.Layout(width = "auto"))
        self._fld_sing_ins = w.Text(layout = w.Layout(width = "auto"))
        self._fld_sing_pre = w.Text(layout = w.Layout(width = "auto"))
        self._fld_plur_nom = w.Text(layout = w.Layout(width = "auto"))
        self._fld_plur_gen = w.Text(layout = w.Layout(width = "auto"))
        self._fld_plur_dat = w.Text(layout = w.Layout(width = "auto"))
        self._fld_plur_acc = w.Text(layout = w.Layout(width = "auto"))
        self._fld_plur_ins = w.Text(layout = w.Layout(width = "auto"))
        self._fld_plur_pre = w.Text(layout = w.Layout(width = "auto"))

        self.add_sections({
            "Singular": {
                "Nominative": self._fld_sing_nom,
                "Genative": self._fld_sing_gen,
                "Accusative": self._fld_sing_dat,
                "Dative": self._fld_sing_acc,
                "Prepositional": self._fld_sing_ins,
                "Instrumental": self._fld_sing_pre,
            },
            "Plural": {
                "Nominative": self._fld_plur_nom,
                "Genative": self._fld_plur_gen,
                "Accusative": self._fld_plur_dat,
                "Dative": self._fld_plur_acc,
                "Prepositional": self._fld_plur_ins,
                "Instrumental": self._fld_plur_pre,
            },  
        })

        self._grid_g[0, 0] = w.Label("Gender")
        self._grid_g[0, 1:] = self._gender

        self.optional_section.children = [self._grid_g]
        self._wordinfo.observe_dictionary(self.handle_inf_update, "value")

    def open_word(self, word: Noun):
        super().open_word(word)
        self._gender.value = word.gender if word.gender is not None else Nominative.gender(word)
        self._fld_sing_nom.value = word.dictionary_form if word.dictionary_form is not None else ""
        self._fld_sing_gen.value = word.sing_genative if word.sing_genative is not None else ""
        self._fld_sing_dat.value = word.sing_dative if word.sing_dative is not None else ""
        self._fld_sing_acc.value = word.sing_accusative if word.sing_accusative is not None else ""
        self._fld_sing_ins.value = word.sing_instrumental if word.sing_instrumental is not None else ""
        self._fld_sing_pre.value = word.sing_prepositional if word.sing_prepositional is not None else ""
        self._fld_plur_nom.value = word.plural_nominative if word.plural_nominative is not None else ""
        self._fld_plur_gen.value = word.plural_genative if word.plural_genative is not None else ""
        self._fld_plur_dat.value = word.plural_dative if word.plural_dative is not None else ""
        self._fld_plur_acc.value = word.plural_accusative if word.plural_accusative is not None else ""
        self._fld_plur_ins.value = word.plural_instrumental if word.plural_instrumental is not None else ""
        self._fld_plur_pre.value = word.plural_prepositional if word.plural_prepositional is not None else ""

    def handle_inf_update(self, _):
        self._fld_sing_nom.value = self._wordinfo.dictionary

    def handle_save(self, _):
        _out = Noun.from_data(self.base_data())

        _out.gender = self._gender.value
        _out.sing_genative = self._fld_sing_gen.value.lower()
        _out.sing_dative = self._fld_sing_dat.value.lower()
        _out.sing_accusative = self._fld_sing_acc.value.lower()
        _out.sing_instrumental = self._fld_sing_ins.value.lower()
        _out.sing_prepositional = self._fld_sing_pre.value.lower()
        _out.plural_nominative = self._fld_plur_nom.value.lower()
        _out.plural_genative = self._fld_plur_gen.value.lower()
        _out.plural_dative = self._fld_plur_dat.value.lower()
        _out.plural_accusative = self._fld_plur_acc.value.lower()
        _out.plural_instrumental = self._fld_plur_ins.value.lower()
        _out.plural_prepositional = self._fld_plur_pre.value.lower()

        self.save_word(_out)

    def reset(self):
        super().reset()
        self._fld_sing_nom.value = ""
        self._fld_sing_gen.value = ""
        self._fld_sing_dat.value = ""
        self._fld_sing_acc.value = ""
        self._fld_sing_ins.value = ""
        self._fld_sing_pre.value = ""
        self._fld_plur_nom.value = ""
        self._fld_plur_gen.value = ""
        self._fld_plur_dat.value = ""
        self._fld_plur_acc.value = ""
        self._fld_plur_ins.value = ""
        self._fld_plur_pre.value = ""
