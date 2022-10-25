from ._word import Word

class Pronoun(Word):
    class FIELD_KEY(Word.FIELD_KEY):
        '''
        Keys used to store and retrieve pronoun data in glossary files.
        '''
        NOMINATIVE = Word.FIELD_KEY.DICTIONARY_FORM
        GENATIVE = "genative"
        DATIVE = "dative"
        ACCUSATIVE = "accusative"
        INSTRUMENTAL = "instrumental"
        PREPOSITIONAL = "prepositional"
        POSS_MASC_NOM = "poss_masc_nom"
        POSS_MASC_GEN = "poss_masc_gen"
        POSS_MASC_DAT = "poss_masc_dat"
        POSS_MASC_ACC = "poss_masc_acc"
        POSS_MASC_INS = "poss_masc_ins"
        POSS_MASC_PRE = "poss_masc_pre"
        POSS_FEMI_NOM = "poss_femi_nom"
        POSS_FEMI_GEN = "poss_femi_gen"
        POSS_FEMI_DAT = "poss_femi_dat"
        POSS_FEMI_ACC = "poss_femi_acc"
        POSS_FEMI_INS = "poss_femi_ins"
        POSS_FEMI_PRE = "poss_femi_pre"
        POSS_NEUT_NOM = "poss_neut_nom"
        POSS_NEUT_GEN = "poss_neut_gen"
        POSS_NEUT_DAT = "poss_neut_dat"
        POSS_NEUT_ACC = "poss_neut_acc"
        POSS_NEUT_INS = "poss_neut_ins"
        POSS_NEUT_PRE = "poss_neut_pre"
        POSS_PLUR_NOM = "poss_plur_nom"
        POSS_PLUR_GEN = "poss_plur_gen"
        POSS_PLUR_DAT = "poss_plur_dat"
        POSS_PLUR_ACC = "poss_plur_acc"
        POSS_PLUR_INS = "poss_plur_ins"
        POSS_PLUR_PRE = "poss_plur_pre"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.genative = kwargs.get(Pronoun.FIELD_KEY.GENATIVE, None)
        self.dative = kwargs.get(Pronoun.FIELD_KEY.DATIVE, None)
        self.accusative = kwargs.get(Pronoun.FIELD_KEY.ACCUSATIVE, None)
        self.instrumental = kwargs.get(Pronoun.FIELD_KEY.INSTRUMENTAL, None)
        self.prepositional = kwargs.get(Pronoun.FIELD_KEY.PREPOSITIONAL, None)
        self.poss_masc_nom = kwargs.get(Pronoun.FIELD_KEY.POSS_MASC_NOM, None)
        self.poss_masc_gen = kwargs.get(Pronoun.FIELD_KEY.POSS_MASC_GEN, None)
        self.poss_masc_dat = kwargs.get(Pronoun.FIELD_KEY.POSS_MASC_DAT, None)
        self.poss_masc_acc = kwargs.get(Pronoun.FIELD_KEY.POSS_MASC_ACC, None)
        self.poss_masc_ins = kwargs.get(Pronoun.FIELD_KEY.POSS_MASC_INS, None)
        self.poss_masc_pre = kwargs.get(Pronoun.FIELD_KEY.POSS_MASC_PRE, None)
        self.poss_femi_nom = kwargs.get(Pronoun.FIELD_KEY.POSS_FEMI_NOM, None)
        self.poss_femi_gen = kwargs.get(Pronoun.FIELD_KEY.POSS_FEMI_GEN, None)
        self.poss_femi_dat = kwargs.get(Pronoun.FIELD_KEY.POSS_FEMI_DAT, None)
        self.poss_femi_acc = kwargs.get(Pronoun.FIELD_KEY.POSS_FEMI_ACC, None)
        self.poss_femi_ins = kwargs.get(Pronoun.FIELD_KEY.POSS_FEMI_INS, None)
        self.poss_femi_pre = kwargs.get(Pronoun.FIELD_KEY.POSS_FEMI_PRE, None)
        self.poss_neut_nom = kwargs.get(Pronoun.FIELD_KEY.POSS_NEUT_NOM, None)
        self.poss_neut_gen = kwargs.get(Pronoun.FIELD_KEY.POSS_NEUT_GEN, None)
        self.poss_neut_dat = kwargs.get(Pronoun.FIELD_KEY.POSS_NEUT_DAT, None)
        self.poss_neut_acc = kwargs.get(Pronoun.FIELD_KEY.POSS_NEUT_ACC, None)
        self.poss_neut_ins = kwargs.get(Pronoun.FIELD_KEY.POSS_NEUT_INS, None)
        self.poss_neut_pre = kwargs.get(Pronoun.FIELD_KEY.POSS_NEUT_PRE, None)
        self.poss_plur_nom = kwargs.get(Pronoun.FIELD_KEY.POSS_PLUR_NOM, None)
        self.poss_plur_gen = kwargs.get(Pronoun.FIELD_KEY.POSS_PLUR_GEN, None)
        self.poss_plur_dat = kwargs.get(Pronoun.FIELD_KEY.POSS_PLUR_DAT, None)
        self.poss_plur_acc = kwargs.get(Pronoun.FIELD_KEY.POSS_PLUR_ACC, None)
        self.poss_plur_ins = kwargs.get(Pronoun.FIELD_KEY.POSS_PLUR_INS, None)
        self.poss_plur_pre = kwargs.get(Pronoun.FIELD_KEY.POSS_PLUR_PRE, None)

        self.list_prefix = "P"

    def save_data(self):
        _out = super().save_data()
        _out[Pronoun.FIELD_KEY.GENATIVE] = self.genative
        _out[Pronoun.FIELD_KEY.DATIVE] = self.dative
        _out[Pronoun.FIELD_KEY.ACCUSATIVE] = self.accusative
        _out[Pronoun.FIELD_KEY.INSTRUMENTAL] = self.instrumental
        _out[Pronoun.FIELD_KEY.PREPOSITIONAL] = self.prepositional
        _out[Pronoun.FIELD_KEY.POSS_MASC_NOM] = self.poss_masc_nom
        _out[Pronoun.FIELD_KEY.POSS_MASC_GEN] = self.poss_masc_gen
        _out[Pronoun.FIELD_KEY.POSS_MASC_DAT] = self.poss_masc_dat
        _out[Pronoun.FIELD_KEY.POSS_MASC_ACC] = self.poss_masc_acc
        _out[Pronoun.FIELD_KEY.POSS_MASC_INS] = self.poss_masc_ins
        _out[Pronoun.FIELD_KEY.POSS_MASC_PRE] = self.poss_masc_pre
        _out[Pronoun.FIELD_KEY.POSS_FEMI_NOM] = self.poss_femi_nom
        _out[Pronoun.FIELD_KEY.POSS_FEMI_GEN] = self.poss_femi_gen
        _out[Pronoun.FIELD_KEY.POSS_FEMI_DAT] = self.poss_femi_dat
        _out[Pronoun.FIELD_KEY.POSS_FEMI_ACC] = self.poss_femi_acc
        _out[Pronoun.FIELD_KEY.POSS_FEMI_INS] = self.poss_femi_ins
        _out[Pronoun.FIELD_KEY.POSS_FEMI_PRE] = self.poss_femi_pre
        _out[Pronoun.FIELD_KEY.POSS_NEUT_NOM] = self.poss_neut_nom
        _out[Pronoun.FIELD_KEY.POSS_NEUT_GEN] = self.poss_neut_gen
        _out[Pronoun.FIELD_KEY.POSS_NEUT_DAT] = self.poss_neut_dat
        _out[Pronoun.FIELD_KEY.POSS_NEUT_ACC] = self.poss_neut_acc
        _out[Pronoun.FIELD_KEY.POSS_NEUT_INS] = self.poss_neut_ins
        _out[Pronoun.FIELD_KEY.POSS_NEUT_PRE] = self.poss_neut_pre
        _out[Pronoun.FIELD_KEY.POSS_PLUR_NOM] = self.poss_plur_nom
        _out[Pronoun.FIELD_KEY.POSS_PLUR_GEN] = self.poss_plur_gen
        _out[Pronoun.FIELD_KEY.POSS_PLUR_DAT] = self.poss_plur_dat
        _out[Pronoun.FIELD_KEY.POSS_PLUR_ACC] = self.poss_plur_acc
        _out[Pronoun.FIELD_KEY.POSS_PLUR_INS] = self.poss_plur_ins
        _out[Pronoun.FIELD_KEY.POSS_PLUR_PRE] = self.poss_plur_pre
        return _out

    @property
    def nominative(self):
        return self.dictionary_form

    @nominative.setter
    def nominative(self, value):
        self.dictionary_form = value

    @staticmethod
    def from_data(data):
        return Pronoun(**data)
