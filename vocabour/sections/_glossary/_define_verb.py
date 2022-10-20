from logging import PlaceHolder
import ipywidgets as w
from ...grammar import Conjugation
from ...data import Verb

class DefineVerb(w.VBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._REGISTERED_SAVE_WORD = []

        self._grid = w.GridspecLayout(14, 2, layout = w.Layout(max_width = "600px"))

        self._btn_save = w.Button(description = "Save", layout = w.Layout(width = "auto"))
        self._btn_cancel = w.Button(description = "Cancel", layout = w.Layout(width = "auto"))

        self._fld_per_inf = w.Text(layout = w.Layout(width = "auto"), placeholder = "'работать'")
        self._fld_def = w.Text(layout = w.Layout(width = "auto"), placeholder = "'to work'")
        self._fld_per_ya = w.Text(layout = w.Layout(width = "auto"), placeholder = "'работаю'")
        self._fld_per_ti = w.Text(layout = w.Layout(width = "auto"), placeholder = "'работаешь'")
        self._fld_per_vi = w.Text(layout = w.Layout(width = "auto"), placeholder = "'работаете'")
        self._fld_per_on = w.Text(layout = w.Layout(width = "auto"), placeholder = "'работает'")
        self._fld_per_mi = w.Text(layout = w.Layout(width = "auto"), placeholder = "'работаем'")
        self._fld_per_oni = w.Text(layout = w.Layout(width = "auto"), placeholder = "'работают'")
        self._fld_tags = w.Textarea(placeholder = "TAGs", layout = w.Layout(width = "auto", height = "100%"))

        self._grid[0, 0] = w.Label("Infinitive")
        self._grid[1, 0] = w.Label("Definition")
        self._grid[2, 0] = w.Label("Я")
        self._grid[3, 0] = w.Label("Ты")
        self._grid[4, 0] = w.Label("Вы")
        self._grid[5, 0] = w.Label("Он/Она/Оно")
        self._grid[6, 0] = w.Label("Мы")
        self._grid[7, 0] = w.Label("Они")

        self._grid[0, 1] = self._fld_per_inf
        self._grid[1, 1] = self._fld_def
        self._grid[2, 1] = self._fld_per_ya
        self._grid[3, 1] = self._fld_per_ti
        self._grid[4, 1] = self._fld_per_vi
        self._grid[5, 1] = self._fld_per_on
        self._grid[6, 1] = self._fld_per_mi
        self._grid[7, 1] = self._fld_per_oni
        self._grid[8:-1, 0:] = self._fld_tags
        self._grid[-1, 0] = self._btn_save
        self._grid[-1, 1] = self._btn_cancel

        self._fld_per_inf.observe(self.handle_inf_update, "value")
        self._btn_save.on_click(self.handle_save_word)

        self.children = self.widgets

    @property
    def widgets(self):
        return [
            self._grid
        ]

    def on_save(self, func):
        self._REGISTERED_SAVE_WORD.append(func)

    def handle_inf_update(self, _):
        self._fld_per_ya.placeholder = f"{Conjugation.ya(self._fld_per_inf.value)}"
        self._fld_per_ti.placeholder = f"{Conjugation.ti(self._fld_per_inf.value)}"
        self._fld_per_vi.placeholder = f"{Conjugation.vi(self._fld_per_inf.value)}"
        self._fld_per_on.placeholder = f"{Conjugation.on(self._fld_per_inf.value)}"
        self._fld_per_mi.placeholder = f"{Conjugation.mi(self._fld_per_inf.value)}"
        self._fld_per_oni.placeholder = f"{Conjugation.oni(self._fld_per_inf.value)}"

    def handle_save_word(self, _):
        if len(self._REGISTERED_SAVE_WORD) > 0:
            _out = Verb()
            _out.perfect_infinitive = self._fld_per_inf.value
            _out._meaning = self._fld_def.value
            _out._per_ya = self._fld_per_ya.value
            _out._per_ti = self._fld_per_ti.value
            _out._per_vi = self._fld_per_ti.value
            _out._per_mi = self._fld_per_mi.value
            _out._per_on = self._fld_per_on.value
            _out._per_oni = self._fld_per_oni.value
            for f in self._REGISTERED_SAVE_WORD:
                f(_out)
