from __future__ import annotations
from ._word import Word

class Adjective(Word):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list_prefix = "AD"

    def save_data(self):
        _out = super().save_data()
        return _out

    def all_forms(self):
        return [
            self.sg_nom_mas,
            self.sg_nom_fem,
            self.sg_nom_neu,
            self.pl_nom,
            self.sg_pre_mas,
            self.sg_pre_fem,
            self.sg_acc_neu,
        ]

    @staticmethod
    def from_data(data):
        return Adjective(**data)

    @property
    def sg_nom_mas(self):
        return self.dictionary_form

    @property
    def sg_nom_fem(self):
        return Adjective.get_sg_nom_fem(self)
    @staticmethod
    def get_sg_nom_fem(word: Adjective):
        _base: str = word.dictionary_form
        return _base[:-2] + "ая" if not _base.endswith("ний") else _base[:-2] + "яя"

    @property
    def sg_nom_neu(self):
        return Adjective.get_sg_nom_neu(self)
    @staticmethod
    def get_sg_nom_neu(word: Adjective):
        return None

    @property
    def sg_gen_mas(self):
        return Adjective.get_sg_gen_mas(self)
    @staticmethod
    def get_sg_gen_mas(word: Adjective):
        return None

    @property
    def sg_gen_fem(self):
        return Adjective.get_sg_gen_fem(self)
    @staticmethod
    def get_sg_gen_fem(word: Adjective):
        return None

    @property
    def sg_gen_neu(self):
        return Adjective.get_sg_gen_neu(self)
    @staticmethod
    def get_sg_gen_neu(word: Adjective):
        return None

    @property
    def sg_dat_mas(self):
        return Adjective.get_sg_dat_mas(self)
    @staticmethod
    def get_sg_dat_mas(word: Adjective):
        return None

    @property
    def sg_dat_fem(self):
        return Adjective.get_sg_dat_fem(self)
    @staticmethod
    def get_sg_dat_fem(word: Adjective):
        return None

    @property
    def sg_dat_neu(self):
        return Adjective.get_sg_dat_neu(self)
    @staticmethod
    def get_sg_dat_neu(word: Adjective):
        return None

    @property
    def sg_acc_mas(self):
        return Adjective.get_sg_acc_mas(self)
    @staticmethod
    def get_sg_acc_mas(word: Adjective):
        return None

    @property
    def sg_acc_fem(self):
        return Adjective.get_sg_acc_fem(self)
    @staticmethod
    def get_sg_acc_fem(word: Adjective):
        return None

    @property
    def sg_acc_neu(self):
        return Adjective.get_sg_acc_neu(self)
    @staticmethod
    def get_sg_acc_neu(word: Adjective):
        return None

    @property
    def sg_ins_mas(self):
        return Adjective.get_sg_ins_mas(self)
    @staticmethod
    def get_sg_ins_mas(word: Adjective):
        return None

    @property
    def sg_ins_fem(self):
        return Adjective.get_sg_ins_fem(self)
    @staticmethod
    def get_sg_ins_fem(word: Adjective):
        return None

    @property
    def sg_ins_neu(self):
        return Adjective.get_sg_ins_neu(self)
    @staticmethod
    def get_sg_ins_neu(word: Adjective):
        return None

    @property
    def sg_pre_mas(self):
        return Adjective.get_sg_pre_mas(self)
    @staticmethod
    def get_sg_pre_mas(word: Adjective):
        return None

    @property
    def sg_pre_fem(self):
        return Adjective.get_sg_pre_fem(self)
    @staticmethod
    def get_sg_pre_fem(word: Adjective):
        return None

    @property
    def sg_pre_neu(self):
        return Adjective.get_sg_pre_neu(self)
    @staticmethod
    def get_sg_pre_neu(word: Adjective):
        return None

    @property
    def pl_nom(self):
        return Adjective.get_pl_nom(self)
    @staticmethod
    def get_pl_nom(word: Adjective):
        return None

    @property
    def pl_gen(self):
        return Adjective.get_pl_gen(self)
    @staticmethod
    def get_pl_gen(word: Adjective):
        return None

    @property
    def pl_dat(self):
        return Adjective.get_pl_dat(self)
    @staticmethod
    def get_pl_dat(word: Adjective):
        return None

    @property
    def pl_acc(self):
        return Adjective.get_pl_acc(self)
    @staticmethod
    def get_pl_acc(word: Adjective):
        return None

    @property
    def pl_ins(self):
        return Adjective.get_pl_ins(self)
    @staticmethod
    def get_pl_ins(word: Adjective):
        return None

    @property
    def pl_pre(self):
        return Adjective.get_pl_pre(self)
    @staticmethod
    def get_pl_pre(word: Adjective):
        return None
