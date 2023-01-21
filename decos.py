import time
from functools import wraps


def timeit(func):
    @wraps(func)
    def _wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        t1 = time.perf_counter()
        print(f"{func.__name__} took {t1 - t0:.6f}s")
        return result

    print(f"_wrapper.__name__ = {_wrapper.__name__}")
    return _wrapper


@timeit
def useless_calculation():
    total = 0
    for i in range(10_000_000):
        total += 1
        _ = i * i
    return total % 123


if __name__ == "__main__":
    total = useless_calculation()
