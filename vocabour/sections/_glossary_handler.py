from __future__ import annotations
import ipywidgets as w
# from ._base_menu import BaseMenu
from ..types import Word
from typing import Callable

class GlossaryHandler(w.HBox):
    '''
    Accepts and uses glossaries.
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._HANDLERS_EXIT = []
        self._HANDLERS_SAVE = []

        self.IGNORE_EVENTS = False
        self.LOADED_GLOSSARY = []

        self.DISPLAY_GLOSSARY = None

        self._header = w.Box()
        self._footer = w.Box()
        self._content = w.Box()
        self.content_display = w.Box(layout = w.Layout(height = "auto", width = "auto"))
        self.options_display = w.Box(layout = w.Layout(height = "auto", width = "auto"))

        self.children = [
            w.VBox([
                self._header,
                self._content,
                self._footer
            ])
        ]

        # child widgets
        self._btn_main_menu = w.Button(description = "Main Menu")
        self._fld_search = w.Text(placeholder = "Search:", layout = w.Layout(width = "auto"))
        self._word_list = w.Select(layout = w.Layout(height = "auto", width = "auto"))

        # create layout
        self.header = self._btn_main_menu
        self.content = w.VBox([self._fld_search, self.options_display, self._word_list])
        self.children = [*self.children, self.content_display]

        # events
        self._btn_main_menu.on_click(self.handle_main_menu)
        self._word_list.observe(self.handle_select_word, "index")
        self._fld_search.observe(self.handle_search_text, "value")

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

    def load(self, glossary):
        self.IGNORE_EVENTS = True
        if glossary is not None:
            self.LOADED_GLOSSARY = glossary
            self.DISPLAY_GLOSSARY = glossary
        else:
            self.LOADED_GLOSSARY = []
            self.DISPLAY_GLOSSARY = []
        self._sort_glossary()
        self.IGNORE_EVENTS = False

    def handle_select_word(self, _):
        '''
        fires when word is selected from displayed list.
        '''
        pass

    def handle_main_menu(self, _):
        self.save()
        self.content_display.children = []
        self.exit()

    def handle_search_text(self, _ = None):
        self.DISPLAY_GLOSSARY = [w for w in self.LOADED_GLOSSARY if w.match(self._fld_search.value)]
        self._sort_glossary()

    def _sort_glossary(self):
        self.IGNORE_EVENTS = True
        self.DISPLAY_GLOSSARY = sorted(self.DISPLAY_GLOSSARY)
        self._word_list.options = [w.list_view for w in self.DISPLAY_GLOSSARY]
        self._word_list.index = None
        self.IGNORE_EVENTS = False

    def on_exit(self, func: Callable[[GlossaryHandler], None]) -> None:
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
