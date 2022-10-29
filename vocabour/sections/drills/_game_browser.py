import ipywidgets as w
from .._glossary_handler import GlossaryHandler
from ._games._definitions import Definitions

class GameBrowser(GlossaryHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._definitions = Definitions()
        self._btn_defs = w.Button(description = "Definitions")
        self.options_display.children = [self._btn_defs]

        self._btn_defs.on_click(self.handle_def_game)

    def handle_def_game(self, _):
        self._definitions.load_data(self.DISPLAY_GLOSSARY)
        self.content_display.children = [self._definitions]
