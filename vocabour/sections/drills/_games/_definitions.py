import ipywidgets as w
import random as r
import time as t
from ..._base_menu import BaseMenu

class Definitions(BaseMenu):
    def __init__(self):
        super().__init__()
        self.CURRENT_ANSWER = None
        self.POSSIBLE_QUESTIONS = []
        self.attempts = 0
        self.correct = 0

        self._display_word = w.HTML()
        self._display_stats = w.HTML()

        self._btn_ans_1 = w.Button(
            description = "1", 
            layout = w.Layout(height='auto', width='auto'))

        self._btn_ans_2 = w.Button(
            description = "2", 
            layout = w.Layout(height='auto', width='auto'))

        self._btn_ans_3 = w.Button(
            description = "3", 
            layout = w.Layout(height='auto', width='auto'))

        self._btn_ans_4 = w.Button(
            description = "4", 
            layout = w.Layout(height='auto', width='auto'))

        self._grid_btns = w.TwoByTwoLayout(
            top_left = self._btn_ans_1,
            top_right = self._btn_ans_2,
            bottom_left = self._btn_ans_3,
            bottom_right = self._btn_ans_4,
        )

        _game = w.GridspecLayout(3, 2)
        _game[0, 1] = self._display_stats
        _game[1, 0:] = self._display_word
        _game[2, 0:] = self._grid_btns

        self.content = _game

        for b in self.answer_buttons:
            b.on_click(self.handle_answer)

    @property
    def answer_buttons(self):
        return [
            self._btn_ans_1,
            self._btn_ans_2,
            self._btn_ans_3,
            self._btn_ans_4,
        ]

    def load_data(self, data):
        self.attempts = 0
        self.correct = 0
        self.LOADED_GLOSSARY = data

        self.POSSIBLE_QUESTIONS = [i for i in self.LOADED_GLOSSARY]

        self.set_up()

    def set_up(self):
        if len(self.POSSIBLE_QUESTIONS) < 1:
            self.POSSIBLE_QUESTIONS = [i for i in self.LOADED_GLOSSARY]

        _order = r.choice((0, 1))

        _choices = r.sample(self.LOADED_GLOSSARY, 4)
        self.CURRENT_ANSWER = r.choice(self.POSSIBLE_QUESTIONS)
        self.CURRENT_ANSWER.attempts += 1

        if self.CURRENT_ANSWER not in _choices:
            _choices.remove(r.choice(_choices))
            _choices.append(self.CURRENT_ANSWER)

        r.shuffle(_choices)

        for i, b in enumerate(self.answer_buttons):
            b.button_style = ""
            b.answer = _choices[i]
            if _order == 0:
                b.description = b.answer.dictionary_form
            else:
                b.description = b.answer.definition

        if _order == 0:
            _prompt = self.CURRENT_ANSWER.definition
        else:
            _prompt = self.CURRENT_ANSWER.dictionary_form

        _num = len(self.POSSIBLE_QUESTIONS)
        _num_phrase = f"{_num} terms" if _num > 1 else "1 term"

        self._display_word.value = f"<center><h1>{_prompt}</h1></center>"
        self._display_stats.value = f"<p align=\"right\">{_num_phrase} remaining.</p>"
        if self.attempts <= 0:
            self._display_stats.value += "<p align=\"right\">0%, "
        else:
            _stat = (self.correct / self.attempts) * 100
            self._display_stats.value += f"<p align=\"right\">{_stat:.1f}%, "
        self._display_stats.value += f"{self.correct}/{self.attempts}</p>"

    def handle_answer(self, btn):
        self.attempts += 1

        if btn.answer is self.CURRENT_ANSWER:
            self.POSSIBLE_QUESTIONS.remove(btn.answer)
            self.CURRENT_ANSWER.correct += 1
            btn.button_style = "success"
            self.correct += 1
        else:
            btn.button_style = "danger"
            for b in self.answer_buttons:
                if b.answer == self.CURRENT_ANSWER:
                    b.button_style = "info"

        t.sleep(1)
        self.set_up()
