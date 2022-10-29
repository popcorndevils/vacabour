import ipywidgets as w
from ._base_menu import BaseMenu

class GlossaryHandler(BaseMenu):
    '''
    Accepts and uses glossaries.
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.DISPLAY_GLOSSARY = None

        # child widgets
        self._btn_main_menu = w.Button(
            description = "Main Menu")

        self.content_display = w.Box(layout = w.Layout(height = "auto", width = "auto"))
        self.options_display = w.Box(layout = w.Layout(height = "auto", width = "auto"))

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
        self.save()
        self.content_display.children = []
        self.exit()

    def handle_select_word(self, _):
        '''
        fires when word is selected from displayed list.
        '''
        pass

    def handle_search_text(self, _ = None):
        self.DISPLAY_GLOSSARY = [w for w in self.LOADED_GLOSSARY if w.match(self._fld_search.value)]
        self._sort_glossary()

    def _sort_glossary(self):
        self.IGNORE_EVENTS = True
        self.DISPLAY_GLOSSARY = sorted(self.DISPLAY_GLOSSARY)
        self._word_list.options = [w.list_view for w in self.DISPLAY_GLOSSARY]
        self._word_list.index = None
        self.IGNORE_EVENTS = False
