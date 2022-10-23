from ._word import Word

class Pronoun(Word):
    class FIELD_KEY(Word.FIELD_KEY):
        '''
        Keys used to store and retrieve pronoun data in glossary files.
        '''
        GENATIVE = "genative"
        DATIVE = "dative"
        ACCUSATIVE = "accusative"
        INSTRUMENTAL = "instrumental"
        PREPOSITIONAL = "prepositional"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.genative = kwargs.get(Pronoun.FIELD_KEY.GENATIVE, None)
        self.dative = kwargs.get(Pronoun.FIELD_KEY.DATIVE, None)
        self.accusative = kwargs.get(Pronoun.FIELD_KEY.ACCUSATIVE, None)
        self.instrumental = kwargs.get(Pronoun.FIELD_KEY.INSTRUMENTAL, None)
        self.prepositional = kwargs.get(Pronoun.FIELD_KEY.PREPOSITIONAL, None)

    def save_data(self):
        _out = super().save_data()

        _out[Pronoun.FIELD_KEY.GENATIVE] = self.genative
        _out[Pronoun.FIELD_KEY.DATIVE] = self.dative
        _out[Pronoun.FIELD_KEY.ACCUSATIVE] = self.accusative
        _out[Pronoun.FIELD_KEY.INSTRUMENTAL] = self.instrumental
        _out[Pronoun.FIELD_KEY.PREPOSITIONAL] = self.prepositional

        return _out

    @staticmethod
    def from_data(data):
        return Pronoun(**data)
