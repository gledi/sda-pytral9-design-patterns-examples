class Operational:
    def serve_homepage(self):
        return "Welcome to the Bank's website"


class Maintenance:
    def serve_homepage(self):
        return "Homepage undergoing maintenance, come back later"


class BankWebsite:
    def __init__(self, mode=Operational):
        self.mode = mode()

    def homepage(self):
        print(self.mode.serve_homepage())


if __name__ == "__main__":
    b = BankWebsite()
    b.homepage()
    b.mode = Maintenance()
    b.homepage()
