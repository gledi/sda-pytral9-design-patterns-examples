class LanguageEnglish:
    _translations = {"cart": "Cart", "profile": "User Profile", "orders": "Your orders"}

    def translate(self, placeholder):
        return self._translations[placeholder]


class LanguagePolish:
    _translations = {"cart": "Wózek", "profile": "Profil", "orders": "Twoje zamówienia"}

    def translate(self, placeholder):
        return self._translations[placeholder]


def get_translation(language="en"):
    translations = {"en": LanguageEnglish, "pl": LanguagePolish}
    return translations[language]()


if __name__ == "__main__":
    en = get_translation()
    pl = get_translation("pl")
    print(en.translate("cart"))
    print(pl.translate("cart"))
