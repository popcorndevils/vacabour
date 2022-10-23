import ipywidgets as w
from .._def_menu import DefMenu
from ._word_info import WordInfo

class Definer(DefMenu):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._btn_save = w.Button(description = "Save", layout = w.Layout(width = "auto"))
        self._btn_cancel = w.Button(description = "Cancel", layout = w.Layout(width = "auto"))

        self._wordinfo = WordInfo()

        self._grid = w.GridspecLayout(1, 2)

        self._grid[0, 0] = self._btn_save
        self._grid[0, 1] = self._btn_cancel

        self.footer = [self._wordinfo.advanced_settings, self._grid]

        self._btn_save.on_click(self.handle_save)
        self._btn_cancel.on_click(lambda _: self.cancel_word())

    def add_options(self, options: dict[str, w.Widget]):
        _display_grid = w.GridspecLayout(2 + len(options), 4)

        _display_grid[0, 0] = w.Label("Dictionary")
        _display_grid[0, 1:] = self._wordinfo.fld_dictionary
        _display_grid[1, 0] = w.Label("Definition")
        _display_grid[1, 1:] = self._wordinfo.fld_definition

        for i, k in enumerate(options.keys()):
            _display_grid[2 + i, 0] = w.Label(k)
            _display_grid[2 + i, 1:] = options[k]

        self.content = _display_grid

    def add_sections(self, options: dict[str, dict[str, w.Widget]]):
        _display_grid = w.GridspecLayout(2, 4)

        _display_grid[0, 0] = w.Label("Dictionary")
        _display_grid[0, 1:] = self._wordinfo.fld_dictionary
        _display_grid[1, 0] = w.Label("Definition")
        _display_grid[1, 1:] = self._wordinfo.fld_definition

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

        self.content = [_display_grid, _display_tabs]

    def handle_save(self, _):
        raise NotImplementedError("handle_save() not implemented.")
