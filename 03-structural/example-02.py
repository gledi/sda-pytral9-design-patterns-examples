class Toast:
    def prepare(self, time):
        return f"Making toast. It will take {time}"


class Juice:
    def pour(self, glasses):
        return f"Pouring {glasses} glasses of juice"


class Eggs:
    def fry(self):
        return f"Frying eggs"


class Breakfast:
    def __init__(self):
        self.toast = Toast()
        self.juice = Juice()
        self.eggs = Eggs()

    def make(self):
        print(self.toast.prepare("5min"))
        print(self.juice.pour(2))
        print(self.eggs.fry())
        print("Breakfast is ready!")


if __name__ == "__main__":
    Breakfast().make()
