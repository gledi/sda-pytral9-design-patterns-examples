"""Defines a decorator to measure execution time of a callable"""
import time

LARGE_NUMBER = 4 ** 39

class TimerDecorator:
    """A decorator to measure execution time"""
    def __init__(self, func):
        self.times = []
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        delta_time = time.time() - start_time
        self.times.append(delta_time)
        print(f"Function {self.func.__name__} has been executed in "
              f"{delta_time}s with the following arguments: {args} {kwargs}")
        return result


@TimerDecorator
def calculate_product_a_million_times(small_number):
    """Dummy calculation"""
    for _ in range(1_000_000):
        _ = LARGE_NUMBER * small_number + small_number ** 39


if __name__ == """__main__""":
    calculate_product_a_million_times(10)
