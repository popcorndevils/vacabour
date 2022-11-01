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
        self._gender.value = word.gender
        self._fld_sing_nom.value = word.dictionary_form if word.dictionary_form is not None else ""
        self._fld_sing_gen.value = word.sg_gen if word.sg_gen is not None else ""
        self._fld_sing_dat.value = word.sg_dat if word.sg_dat is not None else ""
        self._fld_sing_acc.value = word.sg_acc if word.sg_acc is not None else ""
        self._fld_sing_ins.value = word.sg_ins if word.sg_ins is not None else ""
        self._fld_sing_pre.value = word.sg_pre if word.sg_pre is not None else ""
        self._fld_plur_nom.value = word.pl_nom if word.pl_nom is not None else ""
        self._fld_plur_gen.value = word.pl_gen if word.pl_gen is not None else ""
        self._fld_plur_dat.value = word.pl_dat if word.pl_dat is not None else ""
        self._fld_plur_acc.value = word.pl_acc if word.pl_acc is not None else ""
        self._fld_plur_ins.value = word.pl_ins if word.pl_ins is not None else ""
        self._fld_plur_pre.value = word.pl_pre if word.pl_pre is not None else ""

    def handle_inf_update(self, _):
        self._fld_sing_nom.value = self._wordinfo.dictionary
        self._gender.value = Noun.get_gender(self._wordinfo.dictionary)

    def handle_save(self, _):
        _out = Noun.from_data(self.base_data())

        _out.gender = self._gender.value
        _out.sg_gen = self._fld_sing_gen.value.lower()
        _out.sg_dat = self._fld_sing_dat.value.lower()
        _out.sg_acc = self._fld_sing_acc.value.lower()
        _out.sg_ins = self._fld_sing_ins.value.lower()
        _out.sg_pre = self._fld_sing_pre.value.lower()
        _out.pl_nom = self._fld_plur_nom.value.lower()
        _out.pl_gen = self._fld_plur_gen.value.lower()
        _out.pl_dat = self._fld_plur_dat.value.lower()
        _out.pl_acc = self._fld_plur_acc.value.lower()
        _out.pl_ins = self._fld_plur_ins.value.lower()
        _out.pl_pre = self._fld_plur_pre.value.lower()

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
