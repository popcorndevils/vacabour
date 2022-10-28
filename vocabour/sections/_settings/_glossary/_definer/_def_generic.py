from ._base_definer import BaseDefiner

class DefGeneric(BaseDefiner):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
