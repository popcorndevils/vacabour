import ipywidgets as w

class SubMenu(w.VBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._HANDLERS_EXIT = []
        self.IGNORE_EVENTS = False

    def on_exit(self, func):
        '''
        Register function as callback when submenu item closes.  
        Expects handler(sender: SubMenu) -> None
        '''
        self._HANDLERS_EXIT.append(func)

    def exit(self):
        '''
        Call all exit handlers
        '''
        for f in self._HANDLERS_EXIT:
            f(self)
