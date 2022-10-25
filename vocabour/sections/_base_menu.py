from __future__ import annotations
import ipywidgets as w
from ..types import Word
from typing import Callable

class BaseMenu(w.HBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._HANDLERS_EXIT = []
        self._HANDLERS_SAVE = []

        self.IGNORE_EVENTS = False
        self.LOADED_GLOSSARY = []

        self._header = w.Box()
        self._footer = w.Box()
        self._content = w.Box()
        self.children = [
            w.VBox([
                self._header,
                self._content,
                self._footer
            ])
        ]

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
    def footer(self):
        return self._footer.children
    @footer.setter
    def footer(self, value):
        if isinstance(value, list):
            self._footer.children = value
        elif isinstance(value, w.Widget):
            self._footer.children = [value]

    @property
    def content(self):
        return self._content.children
    @content.setter
    def content(self, value):
        if isinstance(value, list):
            self._content.children = value
        elif isinstance(value, w.Widget):
            self._content.children = [value]

    def on_exit(self, func: Callable[[BaseMenu], None]) -> None:
        '''
        Register function as callback when submenu item closes.  
        Expects handler(sender: SubMenu) -> None
        '''
        self._HANDLERS_EXIT.append(func)

    def on_save(self, func: Callable[[list[Word]], None]) -> None:
        '''
        Register function as callback to receive glossary from submenu attempting to save.  
        Expects Callable(glossary: list[Word]) -> None
        '''
        self._HANDLERS_EXIT.append(func)

    def exit(self):
        '''
        Call all exit handlers
        '''
        for f in self._HANDLERS_EXIT:
            f(self)

    def save(self):
        for f in self._HANDLERS_SAVE:
            f(self.LOADED_GLOSSARY)
