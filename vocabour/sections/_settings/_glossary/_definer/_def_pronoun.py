import ipywidgets as w
from ._base_definer import BaseDefiner
from .....types import Pronoun

class DefPronoun(BaseDefiner):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._grid = w.GridspecLayout(5, 4)

        self._fld_nominative = w.Text(layout = w.Layout(width = "auto"), disabled = True)
        self._fld_genative = w.Text(layout = w.Layout(width = "auto"))
        self._fld_accusative = w.Text(layout = w.Layout(width = "auto"))
        self._fld_dative = w.Text(layout = w.Layout(width = "auto"))
        self._fld_prepositional = w.Text(layout = w.Layout(width = "auto"))
        self._fld_instrumental = w.Text(layout = w.Layout(width = "auto"))
        self._fld_poss_masc_nom = w.Text(layout = w.Layout(width = "auto"))
        self._fld_poss_masc_gen = w.Text(layout = w.Layout(width = "auto"))
        self._fld_poss_masc_dat = w.Text(layout = w.Layout(width = "auto"))
        self._fld_poss_masc_acc = w.Text(layout = w.Layout(width = "auto"))
        self._fld_poss_masc_ins = w.Text(layout = w.Layout(width = "auto"))
        self._fld_poss_masc_pre = w.Text(layout = w.Layout(width = "auto"))
        self._fld_poss_femi_nom = w.Text(layout = w.Layout(width = "auto"))
        self._fld_poss_femi_gen = w.Text(layout = w.Layout(width = "auto"))
        self._fld_poss_femi_dat = w.Text(layout = w.Layout(width = "auto"))
        self._fld_poss_femi_acc = w.Text(layout = w.Layout(width = "auto"))
        self._fld_poss_femi_ins = w.Text(layout = w.Layout(width = "auto"))
        self._fld_poss_femi_pre = w.Text(layout = w.Layout(width = "auto"))
        self._fld_poss_neut_nom = w.Text(layout = w.Layout(width = "auto"))
        self._fld_poss_neut_gen = w.Text(layout = w.Layout(width = "auto"))
        self._fld_poss_neut_dat = w.Text(layout = w.Layout(width = "auto"))
        self._fld_poss_neut_acc = w.Text(layout = w.Layout(width = "auto"))
        self._fld_poss_neut_ins = w.Text(layout = w.Layout(width = "auto"))
        self._fld_poss_neut_pre = w.Text(layout = w.Layout(width = "auto"))
        self._fld_poss_plur_nom = w.Text(layout = w.Layout(width = "auto"))
        self._fld_poss_plur_gen = w.Text(layout = w.Layout(width = "auto"))
        self._fld_poss_plur_dat = w.Text(layout = w.Layout(width = "auto"))
        self._fld_poss_plur_acc = w.Text(layout = w.Layout(width = "auto"))
        self._fld_poss_plur_ins = w.Text(layout = w.Layout(width = "auto"))
        self._fld_poss_plur_pre = w.Text(layout = w.Layout(width = "auto"))

        self.add_sections({
            "Standard": {
                "Nominative": self._fld_nominative,
                "Genative": self._fld_genative,
                "Accusative": self._fld_accusative,
                "Dative": self._fld_dative,
                "Prepositional": self._fld_prepositional,
                "Instrumental": self._fld_instrumental,
            },
            "Possessives": {
                "definer_option_subtabs": True,
                "Masculine": {
                    "Nominative": self._fld_poss_masc_nom,
                    "Genative": self._fld_poss_masc_gen,
                    "Dative": self._fld_poss_masc_dat,
                    "Accusative": self._fld_poss_masc_acc,
                    "Instrumentive": self._fld_poss_masc_ins,
                    "Prepositional": self._fld_poss_masc_pre,
                },
                "Feminine": {
                    "Nominative": self._fld_poss_femi_nom,
                    "Genative": self._fld_poss_femi_gen,
                    "Dative": self._fld_poss_femi_dat,
                    "Accusative": self._fld_poss_femi_acc,
                    "Instrumentive": self._fld_poss_femi_ins,
                    "Prepositional": self._fld_poss_femi_pre,
                },
                "Neuter": {
                    "Nominative": self._fld_poss_neut_nom,
                    "Genative": self._fld_poss_neut_gen,
                    "Dative": self._fld_poss_neut_dat,
                    "Accusative": self._fld_poss_neut_acc,
                    "Instrumentive": self._fld_poss_neut_ins,
                    "Prepositional": self._fld_poss_neut_pre,
                },
                "Plural": {
                    "Nominative": self._fld_poss_plur_nom,
                    "Genative": self._fld_poss_plur_gen,
                    "Dative": self._fld_poss_plur_dat,
                    "Accusative": self._fld_poss_plur_acc,
                    "Instrumentive": self._fld_poss_plur_ins,
                    "Prepositional": self._fld_poss_plur_pre,
                },                
            }
        })

        self.observe_dictionary(self.handle_dictionary_update, "value")

    def open_word(self, word: Pronoun):
        super().open_word(word)
        self._fld_genative.value = word.genative if word.genative is not None else ""
        self._fld_dative.value = word.dative if word.dative is not None else ""
        self._fld_accusative.value = word.accusative if word.accusative is not None else ""
        self._fld_instrumental.value = word.instrumental if word.instrumental is not None else ""
        self._fld_prepositional.value = word.prepositional if word.prepositional is not None else ""
        self._fld_poss_masc_nom.value = word.poss_masc_nom if word.poss_masc_nom is not None else ""
        self._fld_poss_masc_gen.value = word.poss_masc_gen if word.poss_masc_gen is not None else ""
        self._fld_poss_masc_dat.value = word.poss_masc_dat if word.poss_masc_dat is not None else ""
        self._fld_poss_masc_acc.value = word.poss_masc_acc if word.poss_masc_acc is not None else ""
        self._fld_poss_masc_ins.value = word.poss_masc_ins if word.poss_masc_ins is not None else ""
        self._fld_poss_masc_pre.value = word.poss_masc_pre if word.poss_masc_pre is not None else ""
        self._fld_poss_femi_nom.value = word.poss_femi_nom if word.poss_femi_nom is not None else ""
        self._fld_poss_femi_gen.value = word.poss_femi_gen if word.poss_femi_gen is not None else ""
        self._fld_poss_femi_dat.value = word.poss_femi_dat if word.poss_femi_dat is not None else ""
        self._fld_poss_femi_acc.value = word.poss_femi_acc if word.poss_femi_acc is not None else ""
        self._fld_poss_femi_ins.value = word.poss_femi_ins if word.poss_femi_ins is not None else ""
        self._fld_poss_femi_pre.value = word.poss_femi_pre if word.poss_femi_pre is not None else ""
        self._fld_poss_neut_nom.value = word.poss_neut_nom if word.poss_neut_nom is not None else ""
        self._fld_poss_neut_gen.value = word.poss_neut_gen if word.poss_neut_gen is not None else ""
        self._fld_poss_neut_dat.value = word.poss_neut_dat if word.poss_neut_dat is not None else ""
        self._fld_poss_neut_acc.value = word.poss_neut_acc if word.poss_neut_acc is not None else ""
        self._fld_poss_neut_ins.value = word.poss_neut_ins if word.poss_neut_ins is not None else ""
        self._fld_poss_neut_pre.value = word.poss_neut_pre if word.poss_neut_pre is not None else ""
        self._fld_poss_plur_nom.value = word.poss_plur_nom if word.poss_plur_nom is not None else ""
        self._fld_poss_plur_gen.value = word.poss_plur_gen if word.poss_plur_gen is not None else ""
        self._fld_poss_plur_dat.value = word.poss_plur_dat if word.poss_plur_dat is not None else ""
        self._fld_poss_plur_acc.value = word.poss_plur_acc if word.poss_plur_acc is not None else ""
        self._fld_poss_plur_ins.value = word.poss_plur_ins if word.poss_plur_ins is not None else ""
        self._fld_poss_plur_pre.value = word.poss_plur_pre if word.poss_plur_pre is not None else ""

    def handle_save(self, _):
        _out = Pronoun.from_data(self._wordinfo.save_data())

        _out.genative = self._fld_genative.value.lower()
        _out.dative = self._fld_dative.value.lower()
        _out.accusative = self._fld_accusative.value.lower()
        _out.instrumental = self._fld_instrumental.value.lower()
        _out.prepositional = self._fld_prepositional.value.lower()
        _out.poss_masc_nom = self._fld_poss_masc_nom.value.lower()
        _out.poss_masc_gen = self._fld_poss_masc_gen.value.lower()
        _out.poss_masc_dat = self._fld_poss_masc_dat.value.lower()
        _out.poss_masc_acc = self._fld_poss_masc_acc.value.lower()
        _out.poss_masc_ins = self._fld_poss_masc_ins.value.lower()
        _out.poss_masc_pre = self._fld_poss_masc_pre.value.lower()
        _out.poss_femi_nom = self._fld_poss_femi_nom.value.lower()
        _out.poss_femi_gen = self._fld_poss_femi_gen.value.lower()
        _out.poss_femi_dat = self._fld_poss_femi_dat.value.lower()
        _out.poss_femi_acc = self._fld_poss_femi_acc.value.lower()
        _out.poss_femi_ins = self._fld_poss_femi_ins.value.lower()
        _out.poss_femi_pre = self._fld_poss_femi_pre.value.lower()
        _out.poss_neut_nom = self._fld_poss_neut_nom.value.lower()
        _out.poss_neut_gen = self._fld_poss_neut_gen.value.lower()
        _out.poss_neut_dat = self._fld_poss_neut_dat.value.lower()
        _out.poss_neut_acc = self._fld_poss_neut_acc.value.lower()
        _out.poss_neut_ins = self._fld_poss_neut_ins.value.lower()
        _out.poss_neut_pre = self._fld_poss_neut_pre.value.lower()
        _out.poss_plur_nom = self._fld_poss_plur_nom.value.lower()
        _out.poss_plur_gen = self._fld_poss_plur_gen.value.lower()
        _out.poss_plur_dat = self._fld_poss_plur_dat.value.lower()
        _out.poss_plur_acc = self._fld_poss_plur_acc.value.lower()
        _out.poss_plur_ins = self._fld_poss_plur_ins.value.lower()
        _out.poss_plur_pre = self._fld_poss_plur_pre.value.lower()

        self.save_word(_out)

    def handle_dictionary_update(self, _):
        self._fld_nominative.value = self.dictionary

    def reset(self):
        super().reset()
        self._fld_genative.value = ""
        self._fld_dative.value = ""
        self._fld_accusative.value = ""
        self._fld_instrumental.value = ""
        self._fld_prepositional.value = ""
        self._fld_poss_masc_nom.value = ""
        self._fld_poss_masc_gen.value = ""
        self._fld_poss_masc_dat.value = ""
        self._fld_poss_masc_acc.value = ""
        self._fld_poss_masc_ins.value = ""
        self._fld_poss_masc_pre.value = ""
        self._fld_poss_femi_nom.value = ""
        self._fld_poss_femi_gen.value = ""
        self._fld_poss_femi_dat.value = ""
        self._fld_poss_femi_acc.value = ""
        self._fld_poss_femi_ins.value = ""
        self._fld_poss_femi_pre.value = ""
        self._fld_poss_neut_nom.value = ""
        self._fld_poss_neut_gen.value = ""
        self._fld_poss_neut_dat.value = ""
        self._fld_poss_neut_acc.value = ""
        self._fld_poss_neut_ins.value = ""
        self._fld_poss_neut_pre.value = ""
        self._fld_poss_plur_nom.value = ""
        self._fld_poss_plur_gen.value = ""
        self._fld_poss_plur_dat.value = ""
        self._fld_poss_plur_acc.value = ""
        self._fld_poss_plur_ins.value = ""
        self._fld_poss_plur_pre.value = ""
