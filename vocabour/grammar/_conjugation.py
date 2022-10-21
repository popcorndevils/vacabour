
class Conjugation:

    @staticmethod
    def ya(verb: str):
        if verb.endswith("ать"):
            return (verb[:-3] + "аю").lower()
        return ""

    @staticmethod
    def ti(verb: str):
        if verb.endswith("ать"):
            return (verb[:-3] + "аешь").lower()
        return ""

    @staticmethod
    def vi(verb: str):
        if verb.endswith("ать"):
            return (verb[:-3] + "аете").lower()
        return ""

    @staticmethod
    def on(verb: str):
        if verb.endswith("ать"):
            return (verb[:-3] + "ает").lower()
        return ""

    @staticmethod
    def mi(verb: str):
        if verb.endswith("ать"):
            return (verb[:-3] + "аем").lower()
        return ""

    @staticmethod
    def oni(verb: str):
        if verb.endswith("ать"):
            return (verb[:-3] + "ают").lower()
        return ""
