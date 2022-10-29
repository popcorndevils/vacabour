import ipywidgets as w
from .._def_menu import DefMenu
from ._word_info import WordInfo
from vocabour.types import Generic

class BaseDefiner(DefMenu):
    def __init__(self, child_type = Generic, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.CHILD_TYPE = child_type

        self._btn_save = w.Button(description = "Save", layout = w.Layout(width = "auto"))
        self._btn_cancel = w.Button(description = "Cancel", layout = w.Layout(width = "auto"))

        self._wordinfo = WordInfo()
        self._addtional_options = w.Box()
        self.optional_section = w.Box()

        _grid_btns = w.GridspecLayout(1, 2)
        _grid_btns[0, 0] = self._btn_save
        _grid_btns[0, 1] = self._btn_cancel

        self._btn_save.on_click(self.handle_save)
        self._btn_cancel.on_click(lambda _: self.cancel_word())

        self._wordinfo.on_submit(self.handle_save)

        self.content = w.VBox([self._wordinfo.grid_default, self.optional_section, self._addtional_options])
        self.footer = [self._wordinfo.advanced_settings, _grid_btns]

    @property
    def dictionary(self):
        return self._wordinfo.dictionary

    def observe_dictionary(self, *args, **kwargs):
        self._wordinfo.observe_dictionary(*args, **kwargs)

    def base_data(self):
        return self._wordinfo.save_data()

    def open_word(self, word):
        super().open_word(word)
        self._wordinfo.open_word(word)

    def add_sections(self, options: dict[str, dict[str, w.Widget]]):
        _sections = {}
        for k in options.keys():
            _tab = options[k]
            if not _tab.get("definer_option_subtabs", False):
                _section_grid = w.GridspecLayout(len(_tab), 4)
                for i, wk in enumerate(_tab.keys()):
                    _section_grid[i, 0] = w.Label(wk)
                    _section_grid[i, 1:] = _tab[wk]
                _sections[k] = _section_grid
            else:
                _inner_menu = {}
                _sub_display_tab = w.Tab()

                for j, wk in enumerate([k for k in _tab.keys() if k != "definer_option_subtabs"]):
                    _sub_tab = _tab[wk]
                    _sub_grid = w.GridspecLayout(len(_sub_tab), 4)
                    for i, swk in enumerate(_sub_tab.keys()):
                        _sub_grid[i, 0] = w.Label(swk)
                        _sub_grid[i, 1:] = _sub_tab[swk]
                    _inner_menu[wk] = _sub_grid

                _sub_display_tab.children = [v for v in _inner_menu.values()]

                for i, name in enumerate(_inner_menu.keys()):
                    _sub_display_tab.set_title(i, name)
                _sections[k] = _sub_display_tab

        _display_tabs = w.Tab()
        _display_tabs.children = [v for v in _sections.values()]

        for i, k in enumerate(_sections.keys()):
            _display_tabs.set_title(i, k)

        self._addtional_options.children = [_display_tabs]

    def handle_save(self, _):
        _out = self.CHILD_TYPE.from_data(self.base_data())
        self.save_word(_out)

    def reset(self):
        self._wordinfo.reset()
