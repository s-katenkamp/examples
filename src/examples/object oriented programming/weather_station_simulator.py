"""
You can use this template to start from.

Both data generating functions are given. The rest must be implemented.
Good Luck!
"""


class WeatherStation:
    def __init__(self, name: str, longitude: float, latitude: float):
        self.name = name
        self.longitude = longitude
        self.latitude = latitude
        self.unit = "not defined"

    def read_data(self) -> float:
        raise NotImplementedError("Subclasses must implement read_data()")

    def convert_unit(self, value: float) -> float:
        return value

    def report(self) -> str:
        raw_value = self.read_data()
        converted_value = self.convert_unit(raw_value)

        return (
            f"Weather station {self.name} at ({self.longitude}, {self.latitude}) "
            f"reports value: {converted_value:.2f} {self.unit}"
        )


class TemperatureSensor(WeatherStation):
    def __init__(self, name: str, longitude: float, latitude: float):
        super().__init__(name, longitude, latitude)
        self.unit = "°C"

    def read_data(self) -> float:
        return self._generate_temperature_data_in_kelvin()

    def convert_unit(self, value: float) -> float:
        return value - 273.15

    def _generate_temperature_data_in_kelvin(self) -> float:
        return 293.15  # Constant for this example


class RainGauge(WeatherStation):
    def __init__(self, name: str, longitude: float, latitude: float):
        super().__init__(name, longitude, latitude)
        self.unit = "mm"

    def read_data(self) -> float:
        return self._generate_rain_data_in_mm()

    def _generate_rain_data_in_mm(self) -> float:
        return 10.0  # Constant for this example


def simulate_reports(stations: list[WeatherStation]) -> list[str]:
    return [station.report() for station in stations]


# Example usage / test
if __name__ == "__main__":
    ts = TemperatureSensor("Hamburg", 10.0, 50.0)
    print(ts.report())

    stations = [
        TemperatureSensor("Berlin Temp", 13.4050, 52.5200),
        RainGauge("Hamburg Rain", 9.9937, 53.5511),
    ]

    for report in simulate_reports(stations):
        print(report)

