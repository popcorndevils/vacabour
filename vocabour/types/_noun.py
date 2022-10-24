from ._word import Word

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
        self.gender = kwargs.get(Noun.FIELD_KEY.GENDER, None)
        self.sing_genative = kwargs.get(Noun.FIELD_KEY.SING_GENATIVE, None)
        self.sing_dative = kwargs.get(Noun.FIELD_KEY.SING_DATIVE, None)
        self.sing_accusative = kwargs.get(Noun.FIELD_KEY.SING_ACCUSATIVE, None)
        self.sing_instrumental = kwargs.get(Noun.FIELD_KEY.SING_INSTRUMENTAL, None)
        self.sing_prepositional = kwargs.get(Noun.FIELD_KEY.SING_PREPOSITIONAL, None)
        self.plural_nominative = kwargs.get(Noun.FIELD_KEY.PLURAL_NOMINATIVE, None)
        self.plural_genative = kwargs.get(Noun.FIELD_KEY.PLURAL_GENATIVE, None)
        self.plural_dative = kwargs.get(Noun.FIELD_KEY.PLURAL_DATIVE, None)
        self.plural_accusative = kwargs.get(Noun.FIELD_KEY.PLURAL_ACCUSATIVE, None)
        self.plural_instrumental = kwargs.get(Noun.FIELD_KEY.PLURAL_INSTRUMENTAL, None)
        self.plural_prepositional = kwargs.get(Noun.FIELD_KEY.PLURAL_PREPOSITIONAL, None)

    def save_data(self):
        _out = super().save_data()
        _out[Noun.FIELD_KEY.GENDER] = self.gender
        _out[Noun.FIELD_KEY.SING_GENATIVE] = self.sing_genative
        _out[Noun.FIELD_KEY.SING_DATIVE] = self.sing_dative
        _out[Noun.FIELD_KEY.SING_ACCUSATIVE] = self.sing_accusative
        _out[Noun.FIELD_KEY.SING_INSTRUMENTAL] = self.sing_instrumental
        _out[Noun.FIELD_KEY.SING_PREPOSITIONAL] = self.sing_prepositional
        _out[Noun.FIELD_KEY.PLURAL_NOMINATIVE] = self.plural_nominative
        _out[Noun.FIELD_KEY.PLURAL_GENATIVE] = self.plural_genative
        _out[Noun.FIELD_KEY.PLURAL_DATIVE] = self.plural_dative
        _out[Noun.FIELD_KEY.PLURAL_ACCUSATIVE] = self.plural_accusative
        _out[Noun.FIELD_KEY.PLURAL_INSTRUMENTAL] = self.plural_instrumental
        _out[Noun.FIELD_KEY.PLURAL_PREPOSITIONAL] = self.plural_prepositional
        return _out

    @property
    def sing_nominative(self):
        return self.dictionary_form

    @sing_nominative.setter
    def sing_nominative(self, value):
        self.dictionary_form = value

    @staticmethod
    def from_data(data):
        return Noun(**data)
