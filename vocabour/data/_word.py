class Word:
    class Type:
        UNDEFINED = "WORD_TYPE_UNDEFINED"
        VERB = "WORD_TYPE_VERB"
        NOUN = "WORD_TYPE_NOUN"

    dictionary_form = None
    definition = None
    type = Type.UNDEFINED
    tags = []

    def __eq__(self, other):
        return self.dictionary_form.lower() == other.dictionary_form.lower()

    def __lt__(self, other):
        return self.dictionary_form.lower() < other.dictionary_form.lower()
