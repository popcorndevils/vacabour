from ._word import Word

class Adjective(Word):
    class FIELD_KEY(Word.FIELD_KEY):
        '''
        Keys used to store and retrieve Adjective data in glossary files.
        '''
        MASC_SING_NOMINATIVE = Word.FIELD_KEY.DICTIONARY_FORM
        MASC_SING_GENATIVE = "masc_sing_genative"
        MASC_SING_DATIVE = "masc_sing_dative"
        MASC_SING_ACCUSATIVE = "masc_sing_accusative"
        MASC_SING_INSTRUMENTAL = "masc_sing_instrumental"
        MASC_SING_PREPOSITIONAL = "masc_sing_prepositional"

        FEM_SING_NOMINATIVE = "fem_sing_nominative"
        FEM_SING_GENATIVE = "fem_sing_genative"
        FEM_SING_DATIVE = "fem_sing_dative"
        FEM_SING_ACCUSATIVE = "fem_sing_accusative"
        FEM_SING_INSTRUMENTAL = "fem_sing_instrumental"
        FEM_SING_PREPOSITIONAL = "fem_sing_prepositional"

        NEUT_SING_NOMINATIVE = "neut_sing_nominative"
        NEUT_SING_GENATIVE = "neut_sing_genative"
        NEUT_SING_DATIVE = "neut_sing_dative"
        NEUT_SING_ACCUSATIVE = "neut_sing_accusative"
        NEUT_SING_INSTRUMENTAL = "neut_sing_instrumental"
        NEUT_SING_PREPOSITIONAL = "neut_sing_prepositional"

        PLURAL_NOMINATIVE = "plural_nominative"
        PLURAL_GENATIVE = "plural_genative"
        PLURAL_DATIVE = "plural_dative"
        PLURAL_ACCUSATIVE = "plural_accusative"
        PLURAL_INSTRUMENTAL = "plural_instrumental"
        PLURAL_PREPOSITIONAL = "plural_prepositional"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.masc_sing_genative = kwargs.get(Adjective.FIELD_KEY.MASC_SING_GENATIVE, None)
        self.masc_sing_dative = kwargs.get(Adjective.FIELD_KEY.MASC_SING_DATIVE, None)
        self.masc_sing_accusative = kwargs.get(Adjective.FIELD_KEY.MASC_SING_ACCUSATIVE, None)
        self.masc_sing_instrumental = kwargs.get(Adjective.FIELD_KEY.MASC_SING_INSTRUMENTAL, None)
        self.masc_sing_prepositional = kwargs.get(Adjective.FIELD_KEY.MASC_SING_PREPOSITIONAL, None)
        self.fem_sing_nominative = kwargs.get(Adjective.FIELD_KEY.FEM_SING_NOMINATIVE, None)
        self.fem_sing_genative = kwargs.get(Adjective.FIELD_KEY.FEM_SING_GENATIVE, None)
        self.fem_sing_dative = kwargs.get(Adjective.FIELD_KEY.FEM_SING_DATIVE, None)
        self.fem_sing_accusative = kwargs.get(Adjective.FIELD_KEY.FEM_SING_ACCUSATIVE, None)
        self.fem_sing_instrumental = kwargs.get(Adjective.FIELD_KEY.FEM_SING_INSTRUMENTAL, None)
        self.fem_sing_prepositional = kwargs.get(Adjective.FIELD_KEY.FEM_SING_PREPOSITIONAL, None)
        self.neut_sing_nominative = kwargs.get(Adjective.FIELD_KEY.NEUT_SING_NOMINATIVE, None)
        self.neut_sing_genative = kwargs.get(Adjective.FIELD_KEY.NEUT_SING_GENATIVE, None)
        self.neut_sing_dative = kwargs.get(Adjective.FIELD_KEY.NEUT_SING_DATIVE, None)
        self.neut_sing_accusative = kwargs.get(Adjective.FIELD_KEY.NEUT_SING_ACCUSATIVE, None)
        self.neut_sing_instrumental = kwargs.get(Adjective.FIELD_KEY.NEUT_SING_INSTRUMENTAL, None)
        self.neut_sing_prepositional = kwargs.get(Adjective.FIELD_KEY.NEUT_SING_PREPOSITIONAL, None)
        self.plural_nominative = kwargs.get(Adjective.FIELD_KEY.PLURAL_NOMINATIVE, None)
        self.plural_genative = kwargs.get(Adjective.FIELD_KEY.PLURAL_GENATIVE, None)
        self.plural_dative = kwargs.get(Adjective.FIELD_KEY.PLURAL_DATIVE, None)
        self.plural_accusative = kwargs.get(Adjective.FIELD_KEY.PLURAL_ACCUSATIVE, None)
        self.plural_instrumental = kwargs.get(Adjective.FIELD_KEY.PLURAL_INSTRUMENTAL, None)
        self.plural_prepositional = kwargs.get(Adjective.FIELD_KEY.PLURAL_PREPOSITIONAL, None)

        self.list_prefix = "AD"

    def save_data(self):
        _out = super().save_data()
        _out[Adjective.FIELD_KEY.MASC_SING_GENATIVE] = self.masc_sing_genative
        _out[Adjective.FIELD_KEY.MASC_SING_DATIVE] = self.masc_sing_dative
        _out[Adjective.FIELD_KEY.MASC_SING_ACCUSATIVE] = self.masc_sing_accusative
        _out[Adjective.FIELD_KEY.MASC_SING_INSTRUMENTAL] = self.masc_sing_instrumental
        _out[Adjective.FIELD_KEY.MASC_SING_PREPOSITIONAL] = self.masc_sing_prepositional
        _out[Adjective.FIELD_KEY.FEM_SING_NOMINATIVE] = self.fem_sing_nominative
        _out[Adjective.FIELD_KEY.FEM_SING_GENATIVE] = self.fem_sing_genative
        _out[Adjective.FIELD_KEY.FEM_SING_DATIVE] = self.fem_sing_dative
        _out[Adjective.FIELD_KEY.FEM_SING_ACCUSATIVE] = self.fem_sing_accusative
        _out[Adjective.FIELD_KEY.FEM_SING_INSTRUMENTAL] = self.fem_sing_instrumental
        _out[Adjective.FIELD_KEY.FEM_SING_PREPOSITIONAL] = self.fem_sing_prepositional
        _out[Adjective.FIELD_KEY.NEUT_SING_NOMINATIVE] = self.neut_sing_nominative
        _out[Adjective.FIELD_KEY.NEUT_SING_GENATIVE] = self.neut_sing_genative
        _out[Adjective.FIELD_KEY.NEUT_SING_DATIVE] = self.neut_sing_dative
        _out[Adjective.FIELD_KEY.NEUT_SING_ACCUSATIVE] = self.neut_sing_accusative
        _out[Adjective.FIELD_KEY.NEUT_SING_INSTRUMENTAL] = self.neut_sing_instrumental
        _out[Adjective.FIELD_KEY.NEUT_SING_PREPOSITIONAL] = self.neut_sing_prepositional
        _out[Adjective.FIELD_KEY.PLURAL_NOMINATIVE] = self.plural_nominative
        _out[Adjective.FIELD_KEY.PLURAL_GENATIVE] = self.plural_genative
        _out[Adjective.FIELD_KEY.PLURAL_DATIVE] = self.plural_dative
        _out[Adjective.FIELD_KEY.PLURAL_ACCUSATIVE] = self.plural_accusative
        _out[Adjective.FIELD_KEY.PLURAL_INSTRUMENTAL] = self.plural_instrumental
        _out[Adjective.FIELD_KEY.PLURAL_PREPOSITIONAL] = self.plural_prepositional
        return _out

    @property
    def masc_sing_nominative(self):
        return self.dictionary_form

    @masc_sing_nominative.setter
    def masc_sing_nominative(self, value):
        self.dictionary_form = value

    @staticmethod
    def from_data(data):
        return Adjective(**data)
