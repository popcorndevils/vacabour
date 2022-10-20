from ._cyrilic._genders import Genders
from ._cyrilic._groups import Groups

class Nominative:
    @staticmethod
    def singular(word):
        return word

    @staticmethod
    def plural(word):
        '''
        Following the default declination rules for russian words, returns the plural form a word.
        '''
        if word.gender == Genders.MASCULINE:
            _sing = word.nominative_singular
            if _sing[-1] in Groups.alcoholic or _sing[-1] in Groups.sizzlers:
                return _sing + "и"
            elif _sing[-1] == "ь" or _sing[-1] == "й":
                return _sing[:-1] + "и"
            else:
                return _sing + "ы"

        elif word.gender == Genders.FEMININE:
            _sing = word.nominative_singular
            if _sing[-1] == "ь" or _sing[-1] == "я":
                return _sing[:-1] + "и"

            elif _sing[-1] == "а":
                if _sing[-2] in Groups.alcoholic or _sing[-2] in Groups.sizzlers:
                    return _sing[:-1] + "и"

            return _sing[:-1] + "ы"

        else:
            _sing = word.nominative_singular
            if _sing[-1] == "е":
                return _sing[:-1] + "я"
            else:
                return _sing[:-1] + "а"
