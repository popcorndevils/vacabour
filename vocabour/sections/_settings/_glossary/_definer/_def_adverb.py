from ._base_definer import BaseDefiner
from .....types import Adverb

class DefAdverb(BaseDefiner):
    def __init__(self, *args, **kwargs):
        super().__init__(Adverb, *args, **kwargs)
