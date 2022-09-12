from abc import ABC, abstractmethod


class Dough(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass


class Sauce(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass


class Cheese(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass


class Veggies(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass


class Pepperoni(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass


class Clams(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass


class ThickCrustDough(Dough):
    def __str__(self) -> str:
        return "ThickCrust style extra thick crust dough"


class ThinCrustDough(Dough):
    def __str__(self) -> str:
        return "Thin Crust Dough"


class PlumTomatoSauce(Sauce):
    def __str__(self) -> str:
        return "Tomato sauce with plum tomatoes"


class MarinaraSauce(Sauce):
    def __str__(self) -> str:
        return "Marinara Sauce"


class MozzarellaCheese(Cheese):
    def __str__(self) -> str:
        return "Shredded Mozzarella"


class ReggianoCheese(Cheese):
    def __str__(self) -> str:
        return "Reggiano Cheese"


class Spinach(Veggies):
    def __str__(self) -> str:
        return "Spinach"


class BlackOlives(Veggies):
    def __str__(self) -> str:
        return "Black Olives"


class Eggplant(Veggies):
    def __str__(self) -> str:
        return "Eggplant"


class Garlic(Veggies):
    def __str__(self) -> str:
        return "Garlic"


class Onion(Veggies):
    def __str__(self) -> str:
        return "Onion"


class Mushroom(Veggies):
    def __str__(self) -> str:
        return "Mushroom"


class RedPepper(Veggies):
    def __str__(self) -> str:
        return "Red Pepper"


class SlicedPepperoni(Pepperoni):
    def __str__(self) -> str:
        return "Sliced Pepperoni"


class FrozenClams(Clams):
    def __str__(self) -> str:
        return "Frozen Clams from Chesapeake Bay"


class FreshClams(Clams):
    def __str__(self) -> str:
        return "Fresh Clams from Long Island Sound"
