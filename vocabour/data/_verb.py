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
