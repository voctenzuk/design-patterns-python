from abc import ABC


class Pizza(ABC):
    _name: str
    _dough: str
    _sauce: str
    _toppings: list[str]

    def prepare(self) -> None:
        print(f"Preparing {self.name}")
        print("Tossing dough...")
        print("Adding sauce...")
        print("Adding toppings: ")
        for topping in self._toppings:
            print(f"\t{topping}")

    def bake(self) -> None:
        print("Bake for 25 minutes at 350")

    def cut(self) -> None:
        print("Cutting the pizza into diagonal slices")

    def box(self) -> None:
        print("Place pizza in official PizzaStore box")

    @property
    def name(self) -> str:
        return self._name

    def __str__(self) -> str:
        result = f"---- {self.name} ----\n"
        if self._dough:
            result += f"{self._dough}\n"
        if self._sauce:
            result += f"{self._sauce}\n"
        if self._toppings:
            result += f"{', '.join(self._toppings)}\n"
        return result


class NYStyleCheesePizza(Pizza):
    def __init__(self) -> None:
        self._name = "NY Style Sauce and Cheese Pizza"
        self._dough = "Thin Crust Dough"
        self._sauce = "Marinara Sauce"
        self._toppings = ["Grated Reggiano Cheese"]


class NYStyleClamPizza(Pizza):
    def __init__(self) -> None:
        self._name = "NY Style Clam Pizza"
        self._dough = "Thin Crust Dough"
        self._sauce = "Marinara Sauce"
        self._toppings = [
            "Grated Reggiano Cheese",
            "Fresh Clams from Long Island Sound",
        ]


class NYStylePepperoniPizza(Pizza):
    def __init__(self) -> None:
        self._name = "NY Style Pepperoni Pizza"
        self._dough = "Thin Crust Dough"
        self._sauce = "Marinara Sauce"
        self._toppings = [
            "Grated Reggiano Cheese",
            "Slices of Pepperoni",
            "Garlic",
            "Onion",
            "Mushrooms",
            "Red Pepper",
        ]


class NYStyleVeggiePizza(Pizza):
    def __init__(self) -> None:
        self._name = "NY Style Veggie Pizza"
        self._dough = "Thin Crust Dough"
        self._sauce = "Marinara Sauce"
        self._toppings = [
            "Grated Reggiano Cheese",
            "Garlic",
            "Onion",
            "Mushrooms",
            "Red Pepper",
        ]


class ChicagoStyleCheesePizza(Pizza):
    def __init__(self) -> None:
        self._name = "Chicago Style Deep Dish Cheese Pizza"
        self._dough = "Extra Thick Crust Dough"
        self._sauce = "Plum Tomato Sauce"
        self._toppings = ["Shredded Mozzarella Cheese"]

    def cut(self) -> None:
        print("Cutting the pizza into square slices")


class ChicagoStyleClamPizza(Pizza):
    def __init__(self) -> None:
        self._name = "Chicago Style Clam Pizza"
        self._dough = "Extra Thick Crust Dough"
        self._sauce = "Plum Tomato Sauce"
        self._toppings = [
            "Shredded Mozzarella Cheese",
            "Frozen Clams from Chesapeake Bay",
        ]

    def cut(self) -> None:
        print("Cutting the pizza into square slices")


class ChicagoStylePepperoniPizza(Pizza):
    def __init__(self) -> None:
        self._name = "Chicago Style Pepperoni Pizza"
        self._dough = "Extra Thick Crust Dough"
        self._sauce = "Plum Tomato Sauce"
        self._toppings = [
            "Shredded Mozzarella Cheese",
            "Black Olives",
            "Spinach",
            "Eggplant",
            "Sliced Pepperoni",
        ]

    def cut(self) -> None:
        print("Cutting the pizza into square slices")


class ChicagoStyleVeggiePizza(Pizza):
    def __init__(self) -> None:
        self._name = "Chicago Style Veggie Pizza"
        self._dough = "Extra Thick Crust Dough"
        self._sauce = "Plum Tomato Sauce"
        self._toppings = [
            "Shredded Mozzarella Cheese",
            "Black Olives",
            "Spinach",
            "Eggplant",
        ]

    def cut(self) -> None:
        print("Cutting the pizza into square slices")
