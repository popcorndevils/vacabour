import ipywidgets as w
import json
import pathlib
from ._game_multiple import GameMultiple

class Vocabour(w.VBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._fld_topics = w.SelectMultiple()
        self._btn_start = w.Button(description = "BEGIN")
        self._game_multi = GameMultiple()

        self.VOCAB = {}
        self.children = self.widgets

        self._btn_start.on_click(self.handle_begin)
        self._game_multi.menu_callback = self.handle_menu_callback

    @property
    def widgets(self):
        return [
            self._fld_topics,
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

    def handle_begin(self, _):
        _topics = None
        if "*" in self._fld_topics.value:
            _topics = self.VOCAB
        else:
            _topics = {k: self.VOCAB[k] for k in self._fld_topics.value}

        if _topics is not None and len(_topics) > 0:
            self._game_multi.load_data(_topics)
            self.children = [self._game_multi]

    def handle_menu_callback(self, _):
        self.children = self.widgets
