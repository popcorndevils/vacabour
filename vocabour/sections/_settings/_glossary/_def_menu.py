import ipywidgets as w

class DefMenu(w.VBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._header = w.Box()
        self._content = w.VBox()
        self._footer = w.VBox()

        self._HANDLERS_SAVE_WORD = []
        self._HANDLERS_CANCEL_WORD = []
        self._EDIT_WORD = None

        self.children = [self._header, self._content, self._footer]

    @property
    def header(self):
        return self._header.children

    @header.setter
    def header(self, value):
        if isinstance(value, list):
            self._header.children = value
        elif isinstance(value, w.Widget):
            self._header.children = [value]

    @property
    def content(self):
        return self._content.children

    @content.setter
    def content(self, value):
        if isinstance(value, list):
            self._content.children = value
        elif isinstance(value, w.Widget):
            self._content.children = [value]

    @property
    def footer(self):
        return self._footer.children

    @footer.setter
    def footer(self, value):
        if isinstance(value, list):
            self._footer.children = value
        elif isinstance(value, w.Widget):
            self._footer.children = [value]

    def on_save_word(self, func):
        self._HANDLERS_SAVE_WORD.append(func)

    def on_cancel_word(self, func):
        self._HANDLERS_CANCEL_WORD.append(func)

    def save_word(self, new_word):
        for f in self._HANDLERS_SAVE_WORD:
            f(new_word, self._EDIT_WORD)
        self._EDIT_WORD = None
        self.reset()

    def new_word(self):
        self._EDIT_WORD = None
        self.reset()

    def cancel_word(self):
        for f in self._HANDLERS_CANCEL_WORD:
            f()

    def open_word(self, word):
        self._EDIT_WORD = word

    def reset(self):
        raise NotImplementedError("reset() not implemented")
