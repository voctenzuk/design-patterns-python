class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class ChocolateBoiler(metaclass=SingletonMeta):
    def __init__(self):
        self.empty = True
        self.boiled = False

    def fill(self):
        if self.is_empty():
            self.empty = False
            self.boiled = False

    def drain(self):
        if not self.is_empty() and self.is_boiled():
            self.empty = True

    def boil(self):
        if not self.is_empty() and not self.is_boiled():
            self.boiled = True

    def is_empty(self):
        return self.empty

    def is_boiled(self):
        return self.boiled
