class Word:
    class FIELD_KEY:
        '''
        Keys used to store and retrieve data in glossary files.
        '''
        DICTIONARY_FORM = "dictionary"
        DEFINITION = "definition"
        ATTEMPTS = "attempts"
        CORRECT = "correct"
        SENTENCE_FORM = "sentence_form"
        TAGS = "tags"

    def __init__(self, *args, **kwargs):
        self.dictionary_form = kwargs.get(Word.FIELD_KEY.DICTIONARY_FORM, None) 
        self.definition = kwargs.get(Word.FIELD_KEY.DEFINITION, None) 
        self.attempts = kwargs.get(Word.FIELD_KEY.ATTEMPTS, 0)
        self.correct = kwargs.get(Word.FIELD_KEY.CORRECT, 0)
        self.sentence_form = kwargs.get(Word.FIELD_KEY.SENTENCE_FORM, None)
        self.tags = kwargs.get(Word.FIELD_KEY.TAGS, []) 

    def __eq__(self, other):
        return self.dictionary_form.lower() == other.dictionary_form.lower()

    def __lt__(self, other):
        return self.dictionary_form.lower() < other.dictionary_form.lower()

    def save_data(self):
        return {
            Word.FIELD_KEY.DICTIONARY_FORM: self.dictionary_form,
            Word.FIELD_KEY.DEFINITION: self.definition,
            Word.FIELD_KEY.ATTEMPTS: self.attempts,
            Word.FIELD_KEY.CORRECT: self.correct,
            Word.FIELD_KEY.SENTENCE_FORM: self.sentence_form,
            Word.FIELD_KEY.TAGS: self.tags,
        }
