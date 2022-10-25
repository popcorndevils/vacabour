import ipywidgets as w
from ._def_manager import DefManager
from ..._sub_menu import SubMenu

class Glossary(SubMenu):
    def __init__(self, *args, **kwargs):
        super().__init__(1, 1, *args, **kwargs)
        self.DISPLAY_GLOSSARY = None
        self._definer = DefManager()

        # child widgets
        self._btn_main_menu = w.Button(
            description = "Main Menu")

        self._fld_search = w.Text(placeholder = "Search:", layout = w.Layout(width = "auto"))

        self._btn_new = w.Button(
            description = "New",
            layout = w.Layout(width = "auto"))

        self._btn_delete = w.Button(
            description = "Delete", 
            layout = w.Layout(width = "auto"))

        self._word_display = w.Box(layout = w.Layout(height = "auto", width = "auto"))
        self._word_list = w.Select(layout = w.Layout(height = "auto", width = "auto"))

        _btns_grid = w.GridspecLayout(1, 2)
        _btns_grid[0, 0] = self._btn_new
        _btns_grid[0, 1] = self._btn_delete

        # create layout
        self.header = self._btn_main_menu

        # self.content[0, :2] = self._fld_search
        # self.content[1, 0] = self._btn_new
        # self.content[1, 1] = self._btn_delete
        # self.content[2:, :2] = self._word_list

        self.content[0, 0] = w.VBox([self._fld_search, _btns_grid, self._word_list])

        self.side_content.children = [self._word_display]
        # self.content[0:, 2:] = self._word_display

        # events
        self._definer.on_save_word(self.handle_save_word)
        self._definer.on_cancel_word(self.handle_cancel)
        self._btn_main_menu.on_click(self.handle_main_menu)
        self._btn_new.on_click(self.handle_new)
        self._btn_delete.on_click(self.handle_delete)
        self._word_list.observe(self.handle_select_word, "index")
        self._fld_search.observe(self.handle_search_text, "value")

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

    def handle_main_menu(self, _):
        self._word_display.children = []
        self.save()
        self.exit()

    def handle_new(self, _):
        self._word_display.children = [self._definer]
        self._definer.new_word()

    def handle_delete(self, _):
        if self._word_list.index is not None:
            _to_rem = self.DISPLAY_GLOSSARY[self._word_list.index]
            self._word_list.index = None
            self.LOADED_GLOSSARY.remove(_to_rem)
            self.handle_search_text()
            self._sort_glossary()
            self.handle_cancel()

    def handle_save_word(self, word, original = None):
        if original:
            self.LOADED_GLOSSARY.remove(original)
        self._word_display.children = []
        self.LOADED_GLOSSARY.append(word)
        self.handle_search_text()

    def handle_cancel(self):
        self._word_list.index = None
        self._word_display.children = []

    def handle_select_word(self, _):
        if self._word_list.index is not None and not self.IGNORE_EVENTS:
            self._definer.open_word(self.DISPLAY_GLOSSARY[self._word_list.index])
            self._word_display.children = [self._definer]

    def handle_search_text(self, _ = None):
        self.DISPLAY_GLOSSARY = [w for w in self.LOADED_GLOSSARY if w.match(self._fld_search.value)]
        self._sort_glossary()

    def _sort_glossary(self):
        self.IGNORE_EVENTS = True
        self.DISPLAY_GLOSSARY = sorted(self.DISPLAY_GLOSSARY)
        self._word_list.options = [w.list_view for w in self.DISPLAY_GLOSSARY]
        self._word_list.index = None
        self.IGNORE_EVENTS = False
