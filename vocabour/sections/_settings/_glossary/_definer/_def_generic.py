from ._base_definer import BaseDefiner
from .....types import Generic

class DefGeneric(BaseDefiner):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle_save(self, _):
        _out = Generic.from_data(self._wordinfo.save_data())
        self.save_word(_out)
