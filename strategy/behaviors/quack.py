from abc import ABC, abstractmethod


class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass


class Quack(QuackBehavior):
    def quack(self):
        print("Quack")


class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak")


class MuteQuack(QuackBehavior):
    def quack(self):
        print("<< Silence >>")
