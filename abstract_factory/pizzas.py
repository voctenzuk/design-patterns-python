from abc import ABC, abstractmethod

import ingredients
from ingredient_factories import PizzaIngredientFactory


class Pizza(ABC):
    _name: str
    _dough: ingredients.Dough
    _sauce: ingredients.Sauce
    _veggies: list[ingredients.Veggies]
    _cheese: ingredients.Cheese
    _pepperoni: ingredients.Pepperoni
    _clam: ingredients.Clams

    @abstractmethod
    def prepare(self) -> None:
        pass

    def bake(self) -> None:
        print("Bake for 25 minutes at 350")

    def cut(self) -> None:
        print("Cutting the pizza into diagonal slices")

    def box(self) -> None:
        print("Place pizza in official PizzaStore box")

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    def __str__(self) -> str:
        result = f"---- {self.name} ----\n"
        if self._dough:
            result += f"{self._dough}\n"
        if self._sauce:
            result += f"{self._sauce}\n"
        if self._cheese:
            result += f"{self._cheese}\n"
        if self._veggies:
            result += f"{', '.join([str(veggie) for veggie in self._veggies])}\n"
        if self._clam:
            result += f"{self._clam}\n"
        if self._pepperoni:
            result += f"{self._pepperoni}\n"
        return result


class CheesePizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory) -> None:
        self._ingredient_factory: PizzaIngredientFactory = ingredient_factory

    def prepare(self) -> None:
        print(f"Preparing {self.name}")
        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()
        self._cheese = self._ingredient_factory.create_cheese()


class ClamPizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory) -> None:
        self._ingredient_factory: PizzaIngredientFactory = ingredient_factory

    def prepare(self) -> None:
        print(f"Preparing {self.name}")
        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()
        self._cheese = self._ingredient_factory.create_cheese()
        self._clam = self._ingredient_factory.create_clam()


class PepperoniPizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory) -> None:
        self._ingredient_factory: PizzaIngredientFactory = ingredient_factory

    def prepare(self) -> None:
        print(f"Preparing {self.name}")
        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()
        self._cheese = self._ingredient_factory.create_cheese()
        self._veggies = self._ingredient_factory.create_veggies()
        self._pepperoni = self._ingredient_factory.create_pepperoni()


class VeggiePizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory) -> None:
        self._ingredient_factory: PizzaIngredientFactory = ingredient_factory

    def prepare(self) -> None:
        print(f"Preparing {self.name}")
        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()
        self._cheese = self._ingredient_factory.create_cheese()
        self._veggies = self._ingredient_factory.create_veggies()
