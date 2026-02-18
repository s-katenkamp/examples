"""Coding Challenge: Design Patterns in Action (Adapter + Composite)."""

from abc import ABC, abstractmethod
import json


# --- Target Interface (Adapter) ---
class WeatherData(ABC):

    @abstractmethod
    def get_temperature(self) -> float:
        pass

    @abstractmethod
    def get_humidity(self) -> float:
        pass


# --- Incompatible Sources ---
class JsonFeed:
    def __init__(self, json_data: str):
        self.data = json.loads(json_data)

    def read_json(self):
        return self.data


class CsvFeed:
    def __init__(self, csv_data: str):
        self.data = csv_data.split(",")  # "temp,humidity"

    def read_csv(self):
        return self.data


# --- Adapters ---
class JsonAdapter(WeatherData):
    def __init__(self, feed: JsonFeed):
        self.feed = feed

    def get_temperature(self) -> float:
        data = self.feed.read_json()
        return float(data["temp"])

    def get_humidity(self) -> float:
        data = self.feed.read_json()
        return float(data["humidity"])


class CsvAdapter(WeatherData):
    def __init__(self, feed: CsvFeed):
        self.feed = feed

    def get_temperature(self) -> float:
        data = self.feed.read_csv()
        return float(data[0])

    def get_humidity(self) -> float:
        data = self.feed.read_csv()
        return float(data[1])


# --- Composite ---
class WeatherComponent(ABC):
    @abstractmethod
    def display(self) -> str:
        pass


class WeatherStation(WeatherComponent):
    def __init__(self, name: str, data: WeatherData):
        self.name = name
        self.data = data

    def display(self) -> str:
        return f"Station {self.name}: Temp={self.data.get_temperature()}°C, Hum={self.data.get_humidity()}%"


class Region(WeatherComponent):
    def __init__(self, name: str):
        self.name = name
        self.components = []

    def add(self, component: WeatherComponent):
        self.components.append(component)

    def remove(self, component: WeatherComponent):
        self.components.remove(component)

    def display(self) -> str:
        result = f"Region {self.name}:"
        for component in self.components:
            result += "\n" + component.display()
        return result
