from abc import ABC, abstractmethod

from weather_data import Observer, WeatherData


class DisplayElement(ABC):
    @abstractmethod
    def display(self) -> None:
        pass


class CurrentConditionsDisplay(Observer, DisplayElement):
    _temperature: float
    _humidity: float

    def __init__(self, weather_data: WeatherData) -> None:
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self, temp: float, humidity: float, pressure: float) -> None:
        self._temperature = temp
        self._humidity = humidity
        self.display()

    def display(self) -> None:
        print(
            f"Current conditions: {self._temperature}"
            f"F degrees and {self._humidity}% humidity"
        )


class StatisticsDisplay(Observer, DisplayElement):
    _num_readings: int = 0
    _max_temp: float = 0.0
    _min_temp: float = 200.0
    _temp_sum: float = 0.0

    def __init__(self, weather_data: WeatherData) -> None:
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self, temp: float, humidity: float, pressure: float) -> None:
        self._temp_sum = temp
        self._num_readings += 1

        if temp > self._max_temp:
            self._max_temp = temp

        if temp < self._min_temp:
            self._min_temp = temp

        self.display()

    def display(self) -> None:
        print(
            f"Avg/Max/Min temperature = {self._temp_sum/self._num_readings}"
            f"/{self._max_temp:.1f}/{self._min_temp:.1f}"
        )


class ForecastDisplay(Observer, DisplayElement):
    _last_pressure: float
    _current_pressure: float = 29.92

    def __init__(self, weather_data: WeatherData) -> None:
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self, temp: float, humidity: float, pressure: float) -> None:
        self._last_pressure = self._current_pressure
        self._current_pressure = pressure
        self.display()

    def display(self) -> None:
        print("Forecast: ", end="")
        if self._current_pressure > self._last_pressure:
            print("Improving weather on the way!")
        elif self._current_pressure == self._last_pressure:
            print("More of the same")
        else:
            print("Watch out for cooler, rainy weather")
