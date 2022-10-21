from ._word import Word

class Noun(Word):
    type = Word.Type.NOUN

    def __init__(self):
        super().__init__()
        self._gender = None
        self._sing_nom = None
        self._plur_nom = None
        self._adjectival = None

    def save_data(self):
        return {
            "type": self.type,
            "dictionary": self.dictionary_form,
            "definition": self.definition,
            "gender": self._gender,
            "sing_nom": self._sing_nom,
            "plur_nom": self._plur_nom,
            "adjectival": self._adjectival,
        }

    @staticmethod
    def from_data(data):
        _out = Noun()
        _out.dictionary_form = data.get("dictionary", None)
        _out.definition = data.get("definition", None)
        _out.gender = data.get("gender", None)
        _out.sing_nom = data.get("sing_nom", None)
        _out.plur_nom = data.get("plur_nom", None)
        _out.adjectival = data.get("adjectival", None)
        return _out
