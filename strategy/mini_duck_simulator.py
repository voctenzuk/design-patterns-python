from behaviors.fly import FlyRocketPowered
from duck import MallardDuck, ModelDuck

if __name__ == "__main__":
    mallard = MallardDuck()
    mallard.perform_quack()
    mallard.perform_fly()

    model = ModelDuck()
    model.perform_fly()
    model.fly_behavior = FlyRocketPowered()
    model.perform_fly()
