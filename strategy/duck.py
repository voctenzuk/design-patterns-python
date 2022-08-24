from abc import ABC, abstractmethod

from behaviors.fly import FlyBehavior, FlyNoWay, FlyWithWings
from behaviors.quack import Quack, QuackBehavior


class Duck(ABC):
    def __init__(
        self, fly_behavior: FlyBehavior, quack_behavior: QuackBehavior
    ) -> None:
        self._fly_behaviour = fly_behavior
        self._quack_behavior = quack_behavior

    @property
    def fly_behavior(self) -> FlyBehavior:
        return self._fly_behaviour

    @fly_behavior.setter
    def fly_behavior(self, fly_behavior: FlyBehavior) -> None:
        self._fly_behaviour = fly_behavior

    @property
    def quack_behavior(self) -> QuackBehavior:
        return self._quack_behavior

    @quack_behavior.setter
    def quack_behavior(self, quack_behavior: QuackBehavior) -> None:
        self._quack_behavior = quack_behavior

    @abstractmethod
    def display(self) -> None:
        pass

    def perform_quack(self) -> None:
        self._quack_behavior.quack()

    def perform_fly(self) -> None:
        self._fly_behaviour.fly()

    def swim(self) -> None:
        print("All ducks float, even decoys!")


class MallardDuck(Duck):
    def __init__(self) -> None:
        super().__init__(FlyWithWings(), Quack())

    def display(self) -> None:
        print("I'm a real Mallard duck")


class ModelDuck(Duck):
    def __init__(self) -> None:
        super().__init__(FlyNoWay(), Quack())

    def display(self) -> None:
        print("I'm a model duck")
