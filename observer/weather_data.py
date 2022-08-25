from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer: "Observer") -> None:
        pass

    @abstractmethod
    def remove_observer(self, observer: "Observer") -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        pass


class Observer(ABC):
    @abstractmethod
    def update(self, temp: float, humidity: float, pressure: float) -> None:
        pass


class WeatherData(Subject):
    _temperature: float
    _humidity: float
    _pressure: float
    _observers: list[Observer]

    def __init__(self) -> None:
        self._observers: list[Observer] = []

    def register_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)

    def measurements_changed(self) -> None:
        self.notify_observers()

    def set_measurements(
        self, temperature: float, humidity: float, pressure: float
    ) -> None:
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.measurements_changed()
