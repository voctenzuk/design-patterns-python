from abc import ABC, abstractmethod

import pizzas


class PizzaStore(ABC):
    def order_pizza(self, pizza_type: str) -> pizzas.Pizza:
        pizza = self.create_pizza(pizza_type)
        print(f"--- Making a {pizza.name} ---")
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    @abstractmethod
    def create_pizza(self, pizza_type: str) -> pizzas.Pizza:
        pass


class NYStylePizzaStore(PizzaStore):
    def create_pizza(self, pizza_type: str) -> pizzas.Pizza:
        if pizza_type == "cheese":
            return pizzas.NYStyleCheesePizza()
        elif pizza_type == "pepperoni":
            return pizzas.NYStylePepperoniPizza()
        elif pizza_type == "clam":
            return pizzas.NYStyleClamPizza()
        elif pizza_type == "veggie":
            return pizzas.NYStyleVeggiePizza()


class ChicagoStylePizzaStore(PizzaStore):
    def create_pizza(self, pizza_type: str) -> pizzas.Pizza:
        if pizza_type == "cheese":
            return pizzas.ChicagoStyleCheesePizza()
        elif pizza_type == "pepperoni":
            return pizzas.ChicagoStylePepperoniPizza()
        elif pizza_type == "clam":
            return pizzas.ChicagoStyleClamPizza()
        elif pizza_type == "veggie":
            return pizzas.ChicagoStyleVeggiePizza()
