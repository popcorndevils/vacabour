from ._word import Word

class Verb(Word):
    class FIELD_KEY(Word.FIELD_KEY):
        '''
        Keys used to store and retrieve verb data in glossary files.
        '''
        IMPERFECT_INF = Word.FIELD_KEY.DICTIONARY_FORM
        IMPERFECT_YA = "imper_ya"
        IMPERFECT_TI = "imper_ti"
        IMPERFECT_VI = "imper_vi"
        IMPERFECT_MI = "imper_mi"
        IMPERFECT_ON = "imper_on"
        IMPERFECT_ONI = "imper_oni"
        PERFECT_INF = "per_inf"
        PERFECT_YA = "per_ya"
        PERFECT_TI = "per_ti"
        PERFECT_VI = "per_vi"
        PERFECT_MI = "per_mi"
        PERFECT_ON = "per_on"
        PERFECT_ONI = "per_oni"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.imper_ya = kwargs.get(Verb.FIELD_KEY.IMPERFECT_YA, None)
        self.imper_ti = kwargs.get(Verb.FIELD_KEY.IMPERFECT_TI, None)
        self.imper_vi = kwargs.get(Verb.FIELD_KEY.IMPERFECT_VI, None)
        self.imper_mi = kwargs.get(Verb.FIELD_KEY.IMPERFECT_MI, None)
        self.imper_on = kwargs.get(Verb.FIELD_KEY.IMPERFECT_ON, None)
        self.imper_oni = kwargs.get(Verb.FIELD_KEY.IMPERFECT_ONI, None)

        self.per_inf = kwargs.get(Verb.FIELD_KEY.PERFECT_INF, None)
        self.per_ya = kwargs.get(Verb.FIELD_KEY.PERFECT_YA, None)
        self.per_ti = kwargs.get(Verb.FIELD_KEY.PERFECT_TI, None)
        self.per_vi = kwargs.get(Verb.FIELD_KEY.PERFECT_VI, None)
        self.per_mi = kwargs.get(Verb.FIELD_KEY.PERFECT_MI, None)
        self.per_on = kwargs.get(Verb.FIELD_KEY.PERFECT_ON, None)
        self.per_oni = kwargs.get(Verb.FIELD_KEY.PERFECT_ONI, None)

        self.list_prefix = "VE"

    def save_data(self):
        _out = super().save_data()
        _out[Verb.FIELD_KEY.IMPERFECT_YA] = self.imper_ya
        _out[Verb.FIELD_KEY.IMPERFECT_TI] = self.imper_ti
        _out[Verb.FIELD_KEY.IMPERFECT_VI] = self.imper_vi
        _out[Verb.FIELD_KEY.IMPERFECT_MI] = self.imper_mi
        _out[Verb.FIELD_KEY.IMPERFECT_ON] = self.imper_on
        _out[Verb.FIELD_KEY.IMPERFECT_ONI] = self.imper_oni
        return _out

    @property
    def imper_inf(self):
        return self.dictionary_form

    @imper_inf.setter
    def imper_inf(self, value):
        self.dictionary_form = value

    @staticmethod
    def from_data(data):
        return Verb(**data)
