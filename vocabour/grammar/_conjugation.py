
class Conjugation:

    @staticmethod
    def ya(verb: str):
        if verb.endswith("ать"):
            return verb[:-3] + "аю"
        return ""

    @staticmethod
    def ti(verb: str):
        if verb.endswith("ать"):
            return verb[:-3] + "аешь"
        return ""

    @staticmethod
    def vi(verb: str):
        if verb.endswith("ать"):
            return verb[:-3] + "аете"
        return ""

    @staticmethod
    def on(verb: str):
        if verb.endswith("ать"):
            return verb[:-3] + "ает"
        return ""

    @staticmethod
    def mi(verb: str):
        if verb.endswith("ать"):
            return verb[:-3] + "аем"
        return ""

    @staticmethod
    def oni(verb: str):
        if verb.endswith("ать"):
            return verb[:-3] + "ают"
        return ""
