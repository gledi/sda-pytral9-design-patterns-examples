import time


class Logger:
    def log(self, msg):
        print(msg)


class WithLevel:
    def __init__(self, log_level, logger):
        self._level = log_level
        self._logger = logger

    def log(self, msg):
        self._logger.log(f"[{self._level}] {msg}")


class WithTimestamp:
    def __init__(self, logger):
        self._logger = logger

    def log(self, msg):
        timestamp = int(time.time())
        self._logger.log(f"{timestamp} {msg}")


if __name__ == "__main__":
    debug = WithTimestamp(WithLevel("DEBUG", Logger()))
    info = WithTimestamp(WithLevel("INFO", Logger()))
    debug.log("Hello")
    info.log("Second log")
