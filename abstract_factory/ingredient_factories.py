from abc import ABC, abstractmethod

import ingredients


class PizzaIngredientFactory(ABC):
    @abstractmethod
    def create_dough(self) -> ingredients.Dough:
        pass

    @abstractmethod
    def create_sauce(self) -> ingredients.Sauce:
        pass

    @abstractmethod
    def create_cheese(self) -> ingredients.Cheese:
        pass

    @abstractmethod
    def create_veggies(self) -> list[ingredients.Veggies]:
        pass

    @abstractmethod
    def create_pepperoni(self) -> ingredients.Pepperoni:
        pass

    @abstractmethod
    def create_clam(self) -> ingredients.Clams:
        pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> ingredients.Dough:
        return ingredients.ThinCrustDough()

    def create_sauce(self) -> ingredients.Sauce:
        return ingredients.MarinaraSauce()

    def create_cheese(self) -> ingredients.Cheese:
        return ingredients.ReggianoCheese()

    def create_veggies(self) -> list[ingredients.Veggies]:
        return [
            ingredients.Garlic(),
            ingredients.Onion(),
            ingredients.Mushroom(),
            ingredients.RedPepper(),
        ]

    def create_pepperoni(self) -> ingredients.Pepperoni:
        return ingredients.SlicedPepperoni()

    def create_clam(self) -> ingredients.Clams:
        return ingredients.FreshClams()


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> ingredients.Dough:
        return ingredients.ThickCrustDough()

    def create_sauce(self) -> ingredients.Sauce:
        return ingredients.PlumTomatoSauce()

    def create_cheese(self) -> ingredients.Cheese:
        return ingredients.MozzarellaCheese()

    def create_veggies(self) -> list[ingredients.Veggies]:
        return [
            ingredients.BlackOlives(),
            ingredients.Spinach(),
            ingredients.Eggplant(),
        ]

    def create_pepperoni(self) -> ingredients.Pepperoni:
        return ingredients.SlicedPepperoni()

    def create_clam(self) -> ingredients.Clams:
        return ingredients.FrozenClams()
