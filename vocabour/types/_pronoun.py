from ._word import Word

class Pronoun(Word):
    type = Word.Type.PRONOUN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.genative = kwargs.get("genative", None)
        self.dative = kwargs.get("dative", None)
        self.accusative = kwargs.get("accusative", None)
        self.instrumental = kwargs.get("instrumental", None)
        self.prepositional = kwargs.get("prepositional", None)

    def save_data(self):
        _out = super().save_data()

        _out["genative"] = self.genative
        _out["dative"] = self.dative
        _out["accusative"] = self.accusative
        _out["instrumental"] = self.instrumental
        _out["prepositional"] = self.prepositional

        return _out

    @staticmethod
    def from_data(data):
        return Pronoun(**data)
