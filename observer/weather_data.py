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
    def update(self) -> None:
        pass


class WeatherData(Subject):
    _temperature: float
    _humidity: float
    _pressure: float
    _observers: list[Observer]

    def __init__(self) -> None:
        self._observers: list[Observer] = []

    @property
    def temperature(self):
        return self._temperature

    @property
    def humidity(self):
        return self._humidity

    @property
    def pressure(self):
        return self._pressure

    def register_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update()

    def measurements_changed(self) -> None:
        self.notify_observers()

    def set_measurements(
        self, temperature: float, humidity: float, pressure: float
    ) -> None:
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.measurements_changed()
