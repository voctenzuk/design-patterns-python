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

    def update(self) -> None:
        self._temperature = self.weather_data.temperature
        self._humidity = self.weather_data.humidity
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

    def update(self) -> None:
        temp = self.weather_data.temperature
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

    def update(self) -> None:
        self._last_pressure = self._current_pressure
        self._current_pressure = self.weather_data.pressure
        self.display()

    def display(self) -> None:
        print("Forecast: ", end="")
        if self._current_pressure > self._last_pressure:
            print("Improving weather on the way!")
        elif self._current_pressure == self._last_pressure:
            print("More of the same")
        else:
            print("Watch out for cooler, rainy weather")


class HeatIndexDisplay(Observer, DisplayElement):
    _heatindex: float

    def __init__(self, weather_data: WeatherData) -> None:
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self) -> None:
        self._heatindex = self.compute_heatindex(
            self.weather_data.temperature, self.weather_data.humidity
        )
        self.display()

    def display(self) -> None:
        print(f"Heat index is {self._heatindex:.4f}")

    @staticmethod
    def compute_heatindex(t: float, rh: float):
        return (
            (16.923 + (0.185212 * t))
            + (5.37941 * rh)
            - (0.100254 * t * rh)
            + (0.00941695 * (t * t))
            + (0.00728898 * (rh * rh))
            + (0.000345372 * (t * t * rh))
            - (0.000814971 * (t * rh * rh))
            + (0.0000102102 * (t * t * rh * rh))
            - (0.000038646 * (t * t * t))
            + (0.0000291583 * (rh * rh * rh))
            + (0.00000142721 * (t * t * t * rh))
            + (0.000000197483 * (t * rh * rh * rh))
            - (0.0000000218429 * (t * t * t * rh * rh))
            + (0.000000000843296 * (t * t * rh * rh * rh))
            - (0.0000000000481975 * (t * t * t * rh * rh * rh))
        )
