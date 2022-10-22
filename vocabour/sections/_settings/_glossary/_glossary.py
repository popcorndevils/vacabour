import ipywidgets as w
from ._def_manager import DefManager
from ..._sub_menu import SubMenu
from ....globals import DATA_FULL_PATH

class Glossary(SubMenu):
    def __init__(self, *args, **kwargs):
        super().__init__(10, 4, *args, **kwargs)

        self._definer = DefManager()

        # child widgets
        self._btn_main_menu = w.Button(
            description = "Main Menu")

        self._btn_new = w.Button(
            description = "New",
            layout = w.Layout(width = "auto"))

        self._btn_delete = w.Button(
            description = "Delete", 
            layout = w.Layout(width = "auto"))
        self._word_display = w.Box(layout = w.Layout(height = "auto", width = "auto"))
        self._word_list = w.Select(layout = w.Layout(height = "auto", width = "auto"))

        # create layout
        self.header = self._btn_main_menu

        self.content[0, 0] = self._btn_new
        self.content[0, 1] = self._btn_delete
        self.content[1:, :2] = self._word_list
        self.content[0:, 2:] = self._word_display

        # events
        self._definer.on_save_word(self.handle_save_word)
        self._definer.on_cancel_word(self.handle_cancel)
        self._btn_main_menu.on_click(self.handle_main_menu)
        self._btn_new.on_click(self.handle_new)
        self._btn_delete.on_click(self.handle_delete)
        self._word_list.observe(self.handle_select_word, "value")

    def load(self, glossary):
        self.IGNORE_EVENTS = True
        if glossary is not None:
            self.LOADED_GLOSSARY = glossary
        else:
            self.LOADED_GLOSSARY = []
        self._sort_glossary()
        self.IGNORE_EVENTS = False

    def handle_main_menu(self, _):
        self._word_display.children = []
        self.save()
        self.exit()

    def handle_new(self, _):
        self._word_display.children = [self._definer]
        self._definer.new_word()

    def handle_delete(self, _):
        if self._word_list.index is not None:
            _torem = self.LOADED_GLOSSARY[self._word_list.index]
            self._word_list.index = None
            self.LOADED_GLOSSARY.remove(_torem)
            self._sort_glossary()
            self.handle_cancel()

    def handle_save_word(self, word, original = None):
        if original:
            self.LOADED_GLOSSARY.remove(original)
        self._word_display.children = []
        self.LOADED_GLOSSARY.append(word)
        self._sort_glossary()

    def handle_cancel(self):
        self._word_list.index = None
        self._word_display.children = []

    def handle_select_word(self, _):
        if self._word_list.index is not None and not self.IGNORE_EVENTS:
            self._definer.open_word(self.LOADED_GLOSSARY[self._word_list.index])
            self._word_display.children = [self._definer]

    def _sort_glossary(self):
        self.IGNORE_EVENTS = True
        self.LOADED_GLOSSARY = sorted(self.LOADED_GLOSSARY)
        self._word_list.options = [w.dictionary_form for w in self.LOADED_GLOSSARY]
        self._word_list.index = None
        self.IGNORE_EVENTS = False
