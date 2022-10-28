from ._base_definer import BaseDefiner
from .....types import Phrase

class DefPhrase(BaseDefiner):
    def __init__(self, *args, **kwargs):
        super().__init__(Phrase, *args, **kwargs)
