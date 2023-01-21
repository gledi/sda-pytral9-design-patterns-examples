from typing import Protocol
import random


class Pillow:
    def __init__(self, filename):
        self.filename = filename

    def resize(self, new_size: tuple[int, int]):
        print(f"resizing {self.filename} to {new_size} ...")


class GraphicsMagick:
    def __init__(self, filename):
        self.filename = filename

    def resize_image(self, width: int, height: int):
        print(f"resizing {self.filename} to {width}x{height} ...")


class AwesomeLib:
    def __init__(self, filename):
        self.filename = filename

    def stretch(self, factor):
        print(f"stretching {self.filename} {factor} times...")


class SupportsImageResize(Protocol):
    def resize(self, new_size: tuple[int, int]) -> None:
        ...


class GraphicsMagickAdapter:
    def __init__(self, filename):
        self.filename = filename
        self._gm = GraphicsMagick(filename)

    def resize(self, new_size: tuple[int, int]) -> None:
        self._gm.resize_image(new_size[0], new_size[1])


class AwesomeLibAdapter:
    def __init__(self, filename):
        self.filename = filename
        self._awesome = AwesomeLib(filename)

    def resize(self, new_size: tuple[int, int]) -> None:
        factor = random.randrange(0, 500) / 100.0
        self._awesome.stretch(factor)
