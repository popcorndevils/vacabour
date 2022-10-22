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
        _out = super().save_data()
        _out["gender"] = self._gender
        _out["sing_nom"] = self._sing_nom
        _out["plur_nom"] = self._plur_nom
        _out["adjectival"] = self._adjectival

    @staticmethod
    def from_data(data):
        return Noun(**data)
