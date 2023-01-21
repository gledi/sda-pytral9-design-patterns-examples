import time


class TwelveStrategy:
    def time(self):
        return time.strftime("%I:%M %p")


class TwentyFourStrategy:
    def time(self):
        return time.strftime("%H:%M")


class Clock:
    def __init__(self, mode=TwentyFourStrategy):
        self.mode = mode()

    def time(self):
        print(f"It's {self.mode.time()}")


if __name__ == "__main__":
    c = Clock()
    c.time()
    c.mode = TwelveStrategy()
    c.time()
