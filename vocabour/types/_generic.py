from ._word import Word

class Generic(Word):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list_prefix = "GE"

    def save_data(self):
        _out = super().save_data()
        return _out

    @staticmethod
    def from_data(data):
        return Generic(**data)
