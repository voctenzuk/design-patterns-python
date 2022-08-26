from abc import ABC, abstractmethod
from enum import Enum


class Size(Enum):
    TALL = 0
    GRANDE = 1
    VENTI = 2


class Beverage(ABC):

    _description: str = "Unknown Beverage"
    _size: Size = Size.TALL

    @property
    def description(self) -> str:
        return self._description

    @property
    def size(self) -> Size:
        return self._size

    @size.setter
    def size(self, size: Size) -> None:
        self._size = size

    @abstractmethod
    def cost(self) -> float:
        pass


class CondimentDecorator(Beverage):
    _beverage: Beverage

    @property
    @abstractmethod
    def description(self) -> str:
        pass

    @property
    def size(self) -> Size:
        return self._beverage.size

    @size.setter
    def size(self, size: Size) -> None:
        self._beverage.size = size


class Espresso(Beverage):
    def __init__(self) -> None:
        self._description = "Espresso"

    def cost(self) -> float:
        return 1.99


class HouseBlend(Beverage):
    def __init__(self) -> None:
        self._description = "House Blend Coffee"

    def cost(self) -> float:
        return 0.89


class DarkRoast(Beverage):
    def __init__(self) -> None:
        self._description = "Dark Roast Coffee"

    def cost(self) -> float:
        return 0.99


class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage) -> None:
        self._beverage = beverage

    @property
    def description(self) -> str:
        return f"{self._beverage.description}, Mocha"

    def cost(self) -> float:
        return self._beverage.cost() + 0.2


class Whip(CondimentDecorator):
    def __init__(self, beverage: Beverage) -> None:
        self._beverage = beverage

    @property
    def description(self) -> str:
        return f"{self._beverage.description}, Whip"

    def cost(self) -> float:
        return self._beverage.cost() + 0.1


class Soy(CondimentDecorator):
    def __init__(self, beverage: Beverage) -> None:
        self._beverage = beverage

    @property
    def description(self) -> str:
        return f"{self._beverage.description}, Soy"

    def cost(self) -> float:
        cost = self._beverage.cost()
        if self._beverage.size == Size.TALL:
            cost += 0.1
        elif self._beverage.size == Size.GRANDE:
            cost += 0.15
        elif self._beverage.size == Size.VENTI:
            cost += 0.2
        return cost


def print_beverage(beverage: Beverage) -> None:
    print(f"{beverage.description} ${beverage.cost()}")


if __name__ == "__main__":
    beverage = Espresso()
    print_beverage(beverage)

    beverage2: Beverage = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print_beverage(beverage2)

    beverage3: Beverage = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3.size = Size.VENTI
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print_beverage(beverage3)
