from chocolate_boiler import ChocolateBoiler

if __name__ == "__main__":
    boiler = ChocolateBoiler()
    boiler.fill()
    boiler.boil()
    boiler.drain()

    boiler2 = ChocolateBoiler()
    boiler2.fill()
    boiler2.boil()
    boiler2.drain()

    boiler3 = ChocolateBoiler()
    boiler3.fill()
    boiler3.boil()
    boiler3.drain()

    boiler4 = ChocolateBoiler()
    boiler4.fill()
    boiler4.boil()
    boiler4.drain()

    print(f"boiler is boiler2? {boiler is boiler2}")
    print(f"boiler2 is boiler3? {boiler2 is boiler3}")
    print(f"boiler3 is boiler4? {boiler3 is boiler4}")
