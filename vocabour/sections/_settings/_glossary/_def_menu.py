from ..._sub_menu import SubMenu

class DefMenu(SubMenu):
    def __init__(self, rows, cols, *args, **kwargs):
        super().__init__(rows, cols, *args, **kwargs)
        self._HANDLERS_SAVE_WORD = []
        self._HANDLERS_CANCEL_WORD = []
        self._EDIT_WORD = None

    def on_save_word(self, func):
        self._HANDLERS_SAVE_WORD.append(func)

    def on_cancel_word(self, func):
        self._HANDLERS_CANCEL_WORD.append(func)

    def save_word(self, new_word):
        for f in self._HANDLERS_SAVE_WORD:
            f(new_word, self._EDIT_WORD)
        self._EDIT_WORD = None

    def new_word(self):
        self._EDIT_WORD = None

    def cancel_word(self):
        for f in self._HANDLERS_CANCEL_WORD:
            f()

    def open_word(self, word):
        self._EDIT_WORD = word
