from __future__ import annotations
from ._word import Word
from ..grammar._cyrilic._groups import Groups
from ..grammar._cyrilic._genders import Genders

class Noun(Word):
    class FIELD_KEY(Word.FIELD_KEY):
        '''
        Keys used to store and retrieve Adjective data in glossary files.
        '''
        SING_NOMINATIVE = Word.FIELD_KEY.DICTIONARY_FORM
        GENDER = "gender"
        SING_GENATIVE = "sing_genative"
        SING_DATIVE = "sing_dative"
        SING_ACCUSATIVE = "sing_accusative"
        SING_INSTRUMENTAL = "sing_instrumental"
        SING_PREPOSITIONAL = "sing_prepositional"

        PLURAL_NOMINATIVE = "plural_nominative"
        PLURAL_GENATIVE = "plural_genative"
        PLURAL_DATIVE = "plural_dative"
        PLURAL_ACCUSATIVE = "plural_accusative"
        PLURAL_INSTRUMENTAL = "plural_instrumental"
        PLURAL_PREPOSITIONAL = "plural_prepositional"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._gender = kwargs.get(Noun.FIELD_KEY.GENDER, None)
        self._sg_gen = kwargs.get(Noun.FIELD_KEY.SING_GENATIVE, None)
        self._sg_dat = kwargs.get(Noun.FIELD_KEY.SING_DATIVE, None)
        self._sg_acc = kwargs.get(Noun.FIELD_KEY.SING_ACCUSATIVE, None)
        self._sg_ins = kwargs.get(Noun.FIELD_KEY.SING_INSTRUMENTAL, None)
        self._sg_pre = kwargs.get(Noun.FIELD_KEY.SING_PREPOSITIONAL, None)
        self._pl_nom = kwargs.get(Noun.FIELD_KEY.PLURAL_NOMINATIVE, None)
        self._pl_gen = kwargs.get(Noun.FIELD_KEY.PLURAL_GENATIVE, None)
        self._pl_dat = kwargs.get(Noun.FIELD_KEY.PLURAL_DATIVE, None)
        self._pl_acc = kwargs.get(Noun.FIELD_KEY.PLURAL_ACCUSATIVE, None)
        self._pl_ins = kwargs.get(Noun.FIELD_KEY.PLURAL_INSTRUMENTAL, None)
        self._pl_pre = kwargs.get(Noun.FIELD_KEY.PLURAL_PREPOSITIONAL, None)

        self.list_prefix = "NO"

    @property
    def gender(self):
        return self._gender if self._gender is not None else Noun.get_gender(self)
    @gender.setter
    def gender(self, value):
        if value is not None:
            self._gender = value

    @property
    def sg_gen(self):
        return self._sg_gen if self._sg_gen is not None else Noun.get_sg_gen(self)
    @sg_gen.setter
    def sg_gen(self, value):
        if value is not None:
            self._sg_gen = value

    @property
    def sg_dat(self):
        return self._sg_dat if self._sg_dat is not None else Noun.get_sg_dat(self)
    @sg_dat.setter
    def sg_dat(self, value):
        if value is not None:
            self._sg_dat = value

    @property
    def sg_acc(self):
        return self._sg_acc if self._sg_acc is not None else Noun.get_sg_acc(self)
    @sg_acc.setter
    def sg_acc(self, value):
        if value is not None:
            self._sg_acc = value

    @property
    def sg_ins(self):
        return self._sg_ins if self._sg_ins is not None else Noun.get_sg_ins(self)
    @sg_ins.setter
    def sg_ins(self, value):
        if value is not None:
            self._sg_ins = value

    @property
    def sg_pre(self):
        return self._sg_pre if self._sg_pre is not None else Noun.get_sg_pre(self)
    @sg_pre.setter
    def sg_pre(self, value):
        if value is not None:
            self._sg_pre = value

    @property
    def pl_nom(self):
        return self._pl_nom if self._pl_nom is not None else Noun.get_pl_nom(self)
    @pl_nom.setter
    def pl_nom(self, value):
        if value is not None:
            self._pl_nom = value

    @property
    def pl_gen(self):
        return self._pl_gen if self._pl_gen is not None else Noun.get_pl_gen(self)
    @pl_gen.setter
    def pl_gen(self, value):
        if value is not None:
            self._pl_gen = value

    @property
    def pl_dat(self):
        return self._pl_dat if self._pl_dat is not None else Noun.get_pl_dat(self)
    @pl_dat.setter
    def pl_dat(self, value):
        if value is not None:
            self._pl_dat = value

    @property
    def pl_acc(self):
        return self._pl_acc if self._pl_acc is not None else Noun.get_pl_acc(self)
    @pl_acc.setter
    def pl_acc(self, value):
        if value is not None:
            self._pl_acc = value

    @property
    def pl_ins(self):
        return self._pl_ins if self._pl_ins is not None else Noun.get_pl_ins(self)
    @pl_ins.setter
    def pl_ins(self, value):
        if value is not None:
            self._pl_ins = value

    @property
    def pl_pre(self):
        return self._pl_pre if self._pl_pre is not None else Noun.get_pl_pre(self)
    @pl_pre.setter
    def pl_pre(self, value):
        if value is not None:
            self._pl_pre = value

    def save_data(self):
        _out = super().save_data()
        _out[Noun.FIELD_KEY.GENDER] = self._gender
        _out[Noun.FIELD_KEY.SING_GENATIVE] = self._sg_gen
        _out[Noun.FIELD_KEY.SING_DATIVE] = self._sg_dat
        _out[Noun.FIELD_KEY.SING_ACCUSATIVE] = self._sg_acc
        _out[Noun.FIELD_KEY.SING_INSTRUMENTAL] = self._sg_ins
        _out[Noun.FIELD_KEY.SING_PREPOSITIONAL] = self._sg_pre
        _out[Noun.FIELD_KEY.PLURAL_NOMINATIVE] = self._pl_nom
        _out[Noun.FIELD_KEY.PLURAL_GENATIVE] = self._pl_gen
        _out[Noun.FIELD_KEY.PLURAL_DATIVE] = self._pl_dat
        _out[Noun.FIELD_KEY.PLURAL_ACCUSATIVE] = self._pl_acc
        _out[Noun.FIELD_KEY.PLURAL_INSTRUMENTAL] = self._pl_ins
        _out[Noun.FIELD_KEY.PLURAL_PREPOSITIONAL] = self._pl_pre
        return _out

    @staticmethod
    def from_data(data):
        return Noun(**data)

    @staticmethod
    def get_gender(word: Noun):
        _last = word.dictionary_form[-1].lower()
        if _last in ["а", "я"]:
            return Genders.FEMININE
        elif _last in ["о", "е"]:
            return Genders.NEUTER
        return Genders.MASCULINE

    @staticmethod
    def get_sg_gen(word: Noun):
        return None

    @staticmethod
    def get_sg_dat(word: Noun):
        return None

    @staticmethod
    def get_sg_acc(word: Noun):
        return None

    @staticmethod
    def get_sg_ins(word: Noun):
        return None

    @staticmethod
    def get_sg_pre(word: Noun):
        return None

    @staticmethod
    def get_pl_nom(word: Noun):
        '''
        return the default plural declination.
        '''
        _sing = word.dictionary_form
        _last = _sing[-1]

        if word.gender == Genders.MASCULINE:
            if _last in Groups.alcoholic or _last in Groups.sizzlers:
                return _sing + "и"
            elif _last == "ь" or _last == "й":
                return _sing[:-1] + "и"
            else:
                return _sing + "ы"

        elif word.gender == Genders.FEMININE:
            if _last == "ь" or _last == "я":
                return _sing[:-1] + "и"

            elif _last == "а":
                if _sing[-2] in Groups.alcoholic or _sing[-2] in Groups.sizzlers:
                    return _sing[:-1] + "и"

            return _sing[:-1] + "ы"

        else:
            _sing = word.nominative_singular
            if _last == "е":
                return _sing[:-1] + "я"
            else:
                return _sing[:-1] + "а"

    @staticmethod
    def get_pl_gen(word: Noun):
        return None

    @staticmethod
    def get_pl_dat(word: Noun):
        return None

    @staticmethod
    def get_pl_acc(word: Noun):
        return None

    @staticmethod
    def get_pl_ins(word: Noun):
        return None

    @staticmethod
    def get_pl_pre(word: Noun):
        return None
