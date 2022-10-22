class Word:
    class Type:
        UNDEFINED = "WORD_TYPE_UNDEFINED"
        VERB = "WORD_TYPE_VERB"
        NOUN = "WORD_TYPE_NOUN"
        PRONOUN = "WORD_TYPE_PRONOUN"

    type = Type.UNDEFINED

    def __init__(self, *args, **kwargs):
        self.dictionary_form = kwargs.get("dictionary", None) 
        self.correct = kwargs.get("correct", 0)
        self.attempts = kwargs.get("attempts", 0)
        self.definition = kwargs.get("definition", None) 
        self.sentence_form = kwargs.get("sentence_form", None)
        self.tags = kwargs.get("tags", []) 

    def __eq__(self, other):
        return self.dictionary_form.lower() == other.dictionary_form.lower()

    def __lt__(self, other):
        return self.dictionary_form.lower() < other.dictionary_form.lower()

    def save_data(self):
        return {
            "attempts": self.attempts,
            "correct": self.correct,
            "dictionary": self.dictionary_form,
            "definition": self.definition,
            "sentence_form": self.sentence_form,
            "tags": self.tags,
        }
