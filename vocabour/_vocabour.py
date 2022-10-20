import ipywidgets as w
import json
import pathlib
from ._game_multiple import GameMultiple
from .sections import Glossary

class Vocabour(w.VBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._btn_start = w.Button(description = "Glossary")
        self._glossary = Glossary()
        self._game_multi = GameMultiple()

        self.VOCAB = {}
        self.children = self.widgets

        self._btn_start.on_click(self.handle_glossary)
        self._game_multi.menu_callback = self.handle_menu_callback

    @property
    def widgets(self):
        return [
            self._btn_start,
        ]

    def load_vocab(self, path, batch = False):
        path_obj = pathlib.Path(path)

        if path_obj.is_dir():
            if batch:
                for x in path_obj.iterdir():
                    with open(x, "rb") as file:
                        self.VOCAB[x.name.replace(".json", "")] = json.load(file)
            else:
                raise IsADirectoryError(f"{path} is a directory, but batch is set to False")

        self._fld_topics.options = ["*", *[k for k in self.VOCAB.keys()]]

    def handle_glossary(self, _):
        self.children = [self._glossary]

    def handle_menu_callback(self, _):
        self.children = self.widgets
