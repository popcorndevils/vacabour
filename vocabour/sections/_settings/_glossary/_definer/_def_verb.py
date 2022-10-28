import ipywidgets as w
from ._base_definer import BaseDefiner
from .....grammar import Conjugation
from .....types import Verb

class DefVerb(BaseDefiner):
    def __init__(self, *args, **kwargs):
        super().__init__(Verb, *args, **kwargs)

        self._fld_imper_ya = w.Text(layout = w.Layout(width = "auto"))
        self._fld_imper_ti = w.Text(layout = w.Layout(width = "auto"))
        self._fld_imper_vi = w.Text(layout = w.Layout(width = "auto"))
        self._fld_imper_on = w.Text(layout = w.Layout(width = "auto"))
        self._fld_imper_mi = w.Text(layout = w.Layout(width = "auto"))
        self._fld_imper_oni = w.Text(layout = w.Layout(width = "auto"))

        self.add_sections({
            "Imperfective": {
                "Я": self._fld_imper_ya,
                "Ты": self._fld_imper_ti,
                "Вы": self._fld_imper_vi,
                "Он/Она/Оно": self._fld_imper_on,
                "Мы": self._fld_imper_mi,
                "Они": self._fld_imper_oni,
            }
        })

        self.reset()

        self.observe_dictionary(self.handle_dictionary_update, "value")

    def open_word(self, word: Verb):
        super().open_word(word)
        self._fld_imper_ya.value = word.imper_ya
        self._fld_imper_ti.value = word.imper_ti
        self._fld_imper_vi.value = word.imper_vi
        self._fld_imper_on.value = word.imper_on
        self._fld_imper_mi.value = word.imper_mi
        self._fld_imper_oni.value = word.imper_oni

    def handle_dictionary_update(self, _):
        _base = self.dictionary

        _ya = Conjugation.ya(_base)
        _ti = Conjugation.ti(_base)
        _vi = Conjugation.vi(_base)
        _on = Conjugation.on(_base)
        _mi = Conjugation.mi(_base)
        _oni = Conjugation.oni(_base)

        self._fld_imper_ya.placeholder = _ya if _ya != "" else "ex: работаю"
        self._fld_imper_ti.placeholder = _ti if _ti != "" else "ex: работаешь"
        self._fld_imper_vi.placeholder = _vi if _vi != "" else "ex: работаете"
        self._fld_imper_on.placeholder = _on if _on != "" else "ex: работает"
        self._fld_imper_mi.placeholder = _mi if _mi != "" else "ex: работаем"
        self._fld_imper_oni.placeholder = _oni if _oni != "" else "ex: работают"

    def handle_save(self, _):
        _out = Verb.from_data(self.base_data()) 

        _out.imper_ya = self._fld_imper_ya.value.lower()
        _out.imper_ti = self._fld_imper_ti.value.lower()
        _out.imper_vi = self._fld_imper_vi.value.lower()
        _out.imper_mi = self._fld_imper_mi.value.lower()
        _out.imper_on = self._fld_imper_on.value.lower()
        _out.imper_oni = self._fld_imper_oni.value.lower()

        self.save_word(_out)

    def reset(self):
        super().reset()
        self._fld_imper_ya.placeholder = "ex: работаю"
        self._fld_imper_ti.placeholder = "ex: работаешь"
        self._fld_imper_vi.placeholder = "ex: работаете"
        self._fld_imper_on.placeholder = "ex: работает"
        self._fld_imper_mi.placeholder = "ex: работаем"
        self._fld_imper_oni.placeholder = "ex: работают"

        self._fld_imper_ya.value = ""
        self._fld_imper_ti.value = ""
        self._fld_imper_vi.value = ""
        self._fld_imper_on.value = ""
        self._fld_imper_mi.value = ""
        self._fld_imper_oni.value = ""
