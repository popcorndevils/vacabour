from ._word import Word

class Noun(Word):
    type = Word.Type.NOUN

    def __init__(self):
        super().__init__()
        self._gender = None
        self._sing_nom = None
        self._plur_nom = None
        self._adjectival = None

    def dictionary_form(self):
        return self._sing_nom.lower()
