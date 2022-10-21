from logging import PlaceHolder
import ipywidgets as w
from ...grammar import Conjugation
from ...vdata import Verb

class DefineVerb(w.VBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._REGISTERED_SAVE_WORD = []
        self._REGISTERED_CANCEL = []

        self._grid = w.GridspecLayout(
            14, 2, layout = w.Layout(max_width = "600px"))

        self._btn_save = w.Button(
            description = "Save",
            layout = w.Layout(width = "auto"))
        self._btn_cancel = w.Button(
            description = "Cancel",
            layout = w.Layout(width = "auto"))

        self._fld_imper_inf = w.Text(layout = w.Layout(width = "auto"))
        self._fld_definition = w.Text(layout = w.Layout(width = "auto"))
        self._fld_imper_ya = w.Text(layout = w.Layout(width = "auto"))
        self._fld_imper_ti = w.Text(layout = w.Layout(width = "auto"))
        self._fld_imper_vi = w.Text(layout = w.Layout(width = "auto"))
        self._fld_imper_on = w.Text(layout = w.Layout(width = "auto"))
        self._fld_imper_mi = w.Text(layout = w.Layout(width = "auto"))
        self._fld_imper_oni = w.Text(layout = w.Layout(width = "auto"))

        self._fld_tags = w.Textarea(
            placeholder = "TAGs",
            layout = w.Layout(width = "auto", height = "100%"))

        self._grid[0, 0] = w.Label("Infinitive")
        self._grid[1, 0] = w.Label("Definition")
        self._grid[2, 0] = w.Label("Я")
        self._grid[3, 0] = w.Label("Ты")
        self._grid[4, 0] = w.Label("Вы")
        self._grid[5, 0] = w.Label("Он/Она/Оно")
        self._grid[6, 0] = w.Label("Мы")
        self._grid[7, 0] = w.Label("Они")

        self._grid[0, 1] = self._fld_imper_inf
        self._grid[1, 1] = self._fld_definition
        self._grid[2, 1] = self._fld_imper_ya
        self._grid[3, 1] = self._fld_imper_ti
        self._grid[4, 1] = self._fld_imper_vi
        self._grid[5, 1] = self._fld_imper_on
        self._grid[6, 1] = self._fld_imper_mi
        self._grid[7, 1] = self._fld_imper_oni
        self._grid[8:-1, 0:] = self._fld_tags
        self._grid[-1, 0] = self._btn_save
        self._grid[-1, 1] = self._btn_cancel

        self._reset()

        self._fld_imper_inf.observe(self.handle_inf_update, "value")
        self._btn_save.on_click(self.handle_save_word)
        self._btn_cancel.on_click(self.handle_cancel)

        self.children = self.widgets

    @property
    def widgets(self):
        return [
            self._grid
        ]

    def on_save(self, func):
        self._REGISTERED_SAVE_WORD.append(func)

    def on_cancel(self, func):
        self._REGISTERED_CANCEL.append(func)

    def new_word(self):
        self._reset()

    def open_word(self, word: Verb):
        self._fld_imper_inf.value = word.dictionary_form
        self._fld_definition.value = word.definition
        self._fld_imper_ya.value = word.imper_ya
        self._fld_imper_ti.value = word.imper_ti
        self._fld_imper_vi.value = word.imper_vi
        self._fld_imper_on.value = word.imper_on
        self._fld_imper_mi.value = word.imper_mi
        self._fld_imper_oni.value = word.imper_oni
        self._fld_tags.value = ", ".join(word.tags)

    def handle_inf_update(self, _):
        _ya = Conjugation.ya(self._fld_imper_inf.value)
        _ti = Conjugation.ti(self._fld_imper_inf.value)
        _vi = Conjugation.vi(self._fld_imper_inf.value)
        _on = Conjugation.on(self._fld_imper_inf.value)
        _mi = Conjugation.mi(self._fld_imper_inf.value)
        _oni = Conjugation.oni(self._fld_imper_inf.value)

        self._fld_imper_ya.placeholder = _ya if _ya != "" else "ex: работаю"
        self._fld_imper_ti.placeholder = _ti if _ti != "" else "ex: работаешь"
        self._fld_imper_vi.placeholder = _vi if _vi != "" else "ex: работаете"
        self._fld_imper_on.placeholder = _on if _on != "" else "ex: работает"
        self._fld_imper_mi.placeholder = _mi if _mi != "" else "ex: работаем"
        self._fld_imper_oni.placeholder = _oni if _oni != "" else "ex: работают"

    def handle_save_word(self, _):
        if len(self._REGISTERED_SAVE_WORD) > 0 and self._fld_imper_inf.value != "":
            _out = Verb()
            _base = self._fld_imper_inf.value.lower()

            _out.dictionary_form = _base
            _out.definition = self._fld_definition.value

            _ya_val = self._fld_imper_ya.value
            _ti_val = self._fld_imper_ti.value
            _vi_val = self._fld_imper_vi.value
            _mi_val = self._fld_imper_mi.value
            _on_val = self._fld_imper_on.value
            _oni_val = self._fld_imper_oni.value

            _out.imper_ya = _ya_val if _ya_val != "" else Conjugation.ya(_base)
            _out.imper_ti = _ti_val if _ti_val != "" else Conjugation.ti(_base)
            _out.imper_vi = _vi_val if _vi_val != "" else Conjugation.vi(_base)
            _out.imper_mi = _mi_val if _mi_val != "" else Conjugation.mi(_base)
            _out.imper_on = _on_val if _on_val != "" else Conjugation.on(_base)
            _out.imper_oni = _oni_val if _oni_val != "" else Conjugation.oni(_base)

            _out.tags = [t.strip() for t in self._fld_tags.value.replace("\n", ",").split(",")]

            for f in self._REGISTERED_SAVE_WORD:
                f(_out)
        else:
            for f in self._REGISTERED_CANCEL:
                f(_out)

        self._reset()

    def handle_cancel(self, _):
        for f in self._REGISTERED_CANCEL:
            f()

    def _reset(self):
        self._fld_imper_inf.placeholder = "ex: работать"
        self._fld_definition.placeholder = "ex: to work"
        self._fld_imper_ya.placeholder = "ex: работаю"
        self._fld_imper_ti.placeholder = "ex: работаешь"
        self._fld_imper_vi.placeholder = "ex: работаете"
        self._fld_imper_on.placeholder = "ex: работает"
        self._fld_imper_mi.placeholder = "ex: работаем"
        self._fld_imper_oni.placeholder = "ex: работают"

        self._fld_imper_inf.value = ""
        self._fld_definition.value = ""
        self._fld_imper_ya.value = ""
        self._fld_imper_ti.value = ""
        self._fld_imper_vi.value = ""
        self._fld_imper_on.value = ""
        self._fld_imper_mi.value = ""
        self._fld_imper_oni.value = ""
        self._fld_tags.value = ""
