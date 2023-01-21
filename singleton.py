class Singleton:
    _instance = None

    def __init__(self, name):
        print(f"- Instance initialization: name={name}")
        self.name = name

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("- Creating new instance")
            cls._instance = object.__new__(cls)
        print("- Returning existing instance")
        return cls._instance
