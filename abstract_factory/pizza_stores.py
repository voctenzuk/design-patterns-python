from abc import ABC, abstractmethod

import pizzas
from ingredient_factories import ChicagoPizzaIngredientFactory, NYPizzaIngredientFactory


class PizzaStore(ABC):
    @abstractmethod
    def create_pizza(self, item: str) -> pizzas.Pizza:
        pass

    def order_pizza(self, pizza_type: str) -> pizzas.Pizza:
        pizza = self.create_pizza(pizza_type)
        print(f"--- Making a {pizza.name} ---")
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


class NYPizzaStore(PizzaStore):
    def create_pizza(self, item: str) -> pizzas.Pizza:
        pizza: pizzas.Pizza = None
        ingredient_factory = NYPizzaIngredientFactory()

        if item == "cheese":
            pizza = pizzas.CheesePizza(ingredient_factory)
            pizza.name = "New York Style Cheese Pizza"
        elif item == "veggie":
            pizza = pizzas.VeggiePizza(ingredient_factory)
            pizza.name = "New York Style Veggie Pizza"
        elif item == "clam":
            pizza = pizzas.ClamPizza(ingredient_factory)
            pizza.name = "New York Style Clam Pizza"
        elif item == "pepperoni":
            pizza = pizzas.PepperoniPizza(ingredient_factory)
            pizza.name = "New York Style Pepperoni Pizza"

        return pizza


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, item: str) -> pizzas.Pizza:
        pizza: pizzas.Pizza = None
        ingredient_factory = ChicagoPizzaIngredientFactory()

        if item == "cheese":
            pizza = pizzas.CheesePizza(ingredient_factory)
            pizza.name = "Chicago Style Deep Dish Cheese Pizza"
        elif item == "veggie":
            pizza = pizzas.VeggiePizza(ingredient_factory)
            pizza.name = "Chicago Style Veggie Pizza"
        elif item == "clam":
            pizza = pizzas.ClamPizza(ingredient_factory)
            pizza.name = "Chicago Style Clam Pizza"
        elif item == "pepperoni":
            pizza = pizzas.PepperoniPizza(ingredient_factory)
            pizza.name = "Chicago Style Pepperoni Pizza"

        return pizza
