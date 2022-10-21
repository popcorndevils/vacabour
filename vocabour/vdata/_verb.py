from ._word import Word

class Verb(Word):
    type = Word.Type.VERB

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.imper_ya = kwargs.get("imper_ya", None)
        self.imper_ti = kwargs.get("imper_ti", None)
        self.imper_vi = kwargs.get("imper_vi", None)
        self.imper_mi = kwargs.get("imper_mi", None)
        self.imper_on = kwargs.get("imper_on", None)
        self.imper_oni = kwargs.get("imper_oni", None)

        self.per_inf = kwargs.get("per_inf", None)
        self.per_ya = kwargs.get("per_ya", None)
        self.per_ti = kwargs.get("per_ti", None)
        self.per_vi = kwargs.get("per_vi", None)
        self.per_mi = kwargs.get("per_mi", None)
        self.per_on = kwargs.get("per_on", None)
        self.per_oni = kwargs.get("per_oni", None)

    def save_data(self):
        _out = super().save_data()
        _out["imper_ya"] = self.imper_ya
        _out["imper_ti"] = self.imper_ti
        _out["imper_vi"] = self.imper_vi
        _out["imper_mi"] = self.imper_mi
        _out["imper_on"] = self.imper_on
        _out["imper_oni"] = self.imper_oni
        return _out

    @staticmethod
    def from_data(data):
        return Verb(**data)
