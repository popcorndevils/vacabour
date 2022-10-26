from ._word import Word

class Adverb(Word):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list_prefix = "AV"

    def save_data(self):
        _out = super().save_data()
        return _out

    @staticmethod
    def from_data(data):
        return Adverb(**data)
