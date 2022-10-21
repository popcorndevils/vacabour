from ._word import Word

class Verb(Word):
    type = Word.Type.VERB

    def __init__(self):
        super().__init__()
        self.imper_ya = None
        self.imper_ti = None
        self.imper_vi = None
        self.imper_mi = None
        self.imper_on = None
        self.imper_oni = None

        self.perfect_infinitive = None
        self.per_ya = None
        self.per_ti = None
        self.per_vi = None
        self.per_mi = None
        self.per_on = None
        self.per_oni = None

    def save_data(self):
        return {
            "type": self.type,
            "dictionary": self.dictionary_form,
            "definition": self.definition,
            "imper_ya": self.imper_ya,
            "imper_ti": self.imper_ti,
            "imper_vi": self.imper_vi,
            "imper_mi": self.imper_mi,
            "imper_on": self.imper_on,
            "imper_oni": self.imper_oni,
        }

    @staticmethod
    def from_data(data):
        _out = Verb()
        _out.dictionary_form = data.get("dictionary", None)
        _out.definition = data.get("definition", None)
        _out.imper_ya = data.get("imper_ya", None)
        _out.imper_ti = data.get("imper_ti", None)
        _out.imper_vi = data.get("imper_vi", None)
        _out.imper_mi = data.get("imper_mi", None)
        _out.imper_on = data.get("imper_on", None)
        _out.imper_oni = data.get("imper_oni", None)
        return _out
