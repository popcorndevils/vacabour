import ipywidgets as w
import random as r
import time as t
from ....types import Adjective
from ..._base_menu import BaseMenu

class Prepositions(BaseMenu):
    def __init__(self):
        super().__init__()
        self._display_word = w.HTML()
        self._display_stats = w.HTML()
        self._selections = w.HBox()

        self.content = self._selections

    def load_data(self, data):
        self.LOADED_GLOSSARY = data
        _words = [w for w in self.LOADED_GLOSSARY if isinstance(w, Adjective)]
        _sample = r.sample(_words, 2)

        _blanks = []

        for s in _sample:
            _blanks.append(w.Dropdown(value = None, options = s.all_forms(), layout = w.Layout(width = "initial")))

        self._selections.children = _blanks

        self.POSSIBLE_QUESTIONS = [i for i in self.LOADED_GLOSSARY]
