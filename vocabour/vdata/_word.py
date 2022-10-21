class Word:
    class Type:
        UNDEFINED = "WORD_TYPE_UNDEFINED"
        VERB = "WORD_TYPE_VERB"
        NOUN = "WORD_TYPE_NOUN"

    type = Type.UNDEFINED

    def __init__(self, *args, **kwargs):
        self.dictionary_form = kwargs.get("dictionary", None) 
        self.definition = kwargs.get("definition", None) 
        self.tags = kwargs.get("tags", []) 

    def __eq__(self, other):
        return self.dictionary_form.lower() == other.dictionary_form.lower()

    def __lt__(self, other):
        return self.dictionary_form.lower() < other.dictionary_form.lower()

    def save_data(self):
        return {
            "dictionary": self.dictionary_form,
            "definition": self.definition,
            "tags": self.tags,
        }
