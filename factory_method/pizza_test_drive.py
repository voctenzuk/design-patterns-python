import pizza_stores

if __name__ == "__main__":
    ny_store = pizza_stores.NYStylePizzaStore()
    chicago_store = pizza_stores.ChicagoStylePizzaStore()

    pizza = ny_store.order_pizza("cheese")
    print(f"Ethan ordered a {pizza.name}\n")

    pizza = chicago_store.order_pizza("cheese")
    print(f"Joel ordered a {pizza.name}\n")

    pizza = ny_store.order_pizza("clam")
    print(f"Ethan ordered a {pizza.name}\n")

    pizza = chicago_store.order_pizza("clam")
    print(f"Joel ordered a {pizza.name}\n")

    pizza = ny_store.order_pizza("pepperoni")
    print(f"Ethan ordered a {pizza.name}\n")

    pizza = chicago_store.order_pizza("pepperoni")
    print(f"Joel ordered a {pizza.name}\n")

    pizza = ny_store.order_pizza("veggie")
    print(f"Ethan ordered a {pizza.name}\n")

    pizza = chicago_store.order_pizza("veggie")
    print(f"Joel ordered a {pizza.name}\n")
