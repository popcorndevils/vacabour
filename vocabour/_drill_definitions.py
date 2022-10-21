import ipywidgets as w
import random as r
import time as t

class DrillDefinitions(w.VBox):
    def __init__(self):
        w.VBox.__init__(self, layout = w.Layout(max_width = "600px"))
        self.CURRENT_ANSWER = None
        self.POSSIBLE_QUESTIONS = []
        self.ALL_QUESTIONS = []
        self.attempts = 0
        self.correct = 0

        self.menu_callback = None
        self._btn_main_menu = w.Button(description = "Main Menu")
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

        self.children = self.widgets

        self._btn_main_menu.on_click(self.handle_main_menu)

        for b in self.answer_buttons:
            b.on_click(self.handle_answer)

    @property
    def widgets(self):
        return [
            self._btn_main_menu,
            self._display_stats,
            self._display_word,
            self._grid_btns,
        ]

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
        self.ALL_QUESTIONS = list(data.items())

        self.POSSIBLE_QUESTIONS = [i for i in self.ALL_QUESTIONS]

        self.set_up()

    def set_up(self):
        if len(self.POSSIBLE_QUESTIONS) < 4:
            self.POSSIBLE_QUESTIONS = [i for i in self.ALL_QUESTIONS]
        _answers = r.sample(self.POSSIBLE_QUESTIONS, 4)
        _order = r.choice(((0, 1), (1, 0)))

        for i, b in enumerate(self.answer_buttons):
            b.button_style = ""
            b.answer = _answers[i]
            b.description = b.answer[_order[0]]

        self.CURRENT_ANSWER = r.choice(self.answer_buttons)
        _prompt = self.CURRENT_ANSWER.answer[_order[1]]
        self._display_word.value = f"<center><h1>{_prompt}</h1></center>"
        if self.attempts <= 0:
            self._display_stats.value = "<p align=\"right\">0%</p>"
        else:
            _stat = (self.correct / self.attempts) * 100
            self._display_stats.value = f"<p align=\"right\">{_stat:.1f}%</p>"

    def handle_answer(self, btn):
        self.attempts += 1

        if btn is self.CURRENT_ANSWER:
            self.POSSIBLE_QUESTIONS.remove(btn.answer)
            btn.button_style = "success"
            self.correct += 1
        else:
            btn.button_style = "danger"
            self.CURRENT_ANSWER.button_style = "info"

        t.sleep(1)
        self.set_up()

    def handle_main_menu(self, _):
        if self.menu_callback is not None:
            self.menu_callback(self)
