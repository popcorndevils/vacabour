import ipywidgets as w
from .._glossary_handler import GlossaryHandler
from ._games._definitions import Definitions
from ._games._prepositions import Prepositions

class GameBrowser(GlossaryHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._definitions = Definitions()
        self._prepositions = Prepositions()

        self._btn_defs = w.Button(description = "Definitions")
        self._btn_preps = w.Button(description = "Prepositions")

        self.options_display.children = [w.HBox([self._btn_defs, self._btn_preps])]

        self._btn_defs.game = self._definitions
        self._btn_preps.game = self._prepositions

        self._btn_defs.on_click(self.handle_start_game)
        self._btn_preps.on_click(self.handle_start_game)

    def handle_start_game(self, btn):
        btn.game.load_data(self.DISPLAY_GLOSSARY)
        self.content_display.children = [btn.game]
