# (ComputerBuilder("Dell XPS 15")
#     .withCPU("Core i7")
#     .withRam("16 GB")
#     .withDisplay("1920x1080")
#     .withHDD("500 GB SSD")
#     .withKeyboardLayout("fr-FR")
#     .withGPU("NVidia Geforce")
#     .withOS("Ubuntu 22.04")
#     .build()
# )
import sys
import datetime


class Computer:
    def __init__(self, model):
        self.model = model
        self.cpu = "Core i3"
        self.ram = 8
        self.display = (1366, 768)
        self.hdd = 500
        self.keyboard = "en-US"
        self.gpu = "Iris"
        self.os = "Windows 10"

    def __str__(self):
        return "\n".join([f"{k}: {v}" for k, v in self.__dict__.items()])


class ComputerBuilder:
    def __init__(self, model):
        self.computer = Computer(model)

    def with_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def with_memory(self, size):
        self.computer.ram = size
        return self

    def with_display(self, width, height):
        self.computer.display = (width, height)
        return self

    def with_hdd(self, size):
        self.computer.hdd = size
        return self

    def with_keyboard(self, language):
        self.computer.keyboard = language
        return self

    def with_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def with_os(self, operating_system):
        self.computer.os = operating_system
        return self

    def build(self):
        return self.computer


class Logger:
    DEBUG = 10
    INFO = 20
    WARN = 30
    ERROR = 40
    CRITICAL = 50
    _level_names = {
        DEBUG: "DEBUG",
        INFO: "INFO",
        WARN: "WARN",
        ERROR: "ERROR",
        CRITICAL: "CRITICAL",
    }

    def __init__(self, name="root"):
        self.name = name
        self.level = self.DEBUG
        self.fmt = "{name}:{ts:%Y-%m-%d %H:%M:%S} - [{level}] {msg}"
        self.destination = sys.stderr

    def __str__(self):
        return self.name

    def log(self, message):
        line = self.fmt.format(
            name=self.name,
            ts=datetime.datetime.utcnow(),
            level=self._level_names.get(self.level, "N/A"),
            msg=message,
        )
        self.destination.write(f"{line}\n")


class LoggerBuilder:
    def __init__(self, name):
        self.logger = Logger(name)

    def with_level(self, level):
        self.logger.level = level
        return self

    def with_format(self, fmt):
        self.logger.fmt = fmt
        return self

    def with_destination(self, dest):
        self.logger.destination = dest
        return self

    def build(self):
        return self.logger
