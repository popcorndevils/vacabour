from ._base_definer import BaseDefiner
from .....types import Adjective

class DefAdjective(BaseDefiner):
    def __init__(self, *args, **kwargs):
        super().__init__(Adjective, *args, **kwargs)
