class Message:
    def __init__(self, text):
        self._text = text

    def __str__(self):
        return self._text


class Capitalized:
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return str(self._msg).capitalize()


class WithExclamation:
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return str(self._msg) + "!"


class WithQuestion:
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return str(self._msg) + "?"


m = Message("really")
happy = Capitalized(WithExclamation(m))
print(str(happy))
confused = Capitalized(WithQuestion(WithExclamation(m)))
print(str(confused))
