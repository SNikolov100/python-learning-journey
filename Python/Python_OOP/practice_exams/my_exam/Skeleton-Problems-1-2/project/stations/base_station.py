from abc import ABC, abstractmethod

from project.astronauts.base_astronaut import BaseAstronaut


class BaseStation(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name            #name of the station
        self.capacity = capacity    #currently available capacity of the station
        self.astronauts: list[BaseAstronaut] = []   #collection of astronauts (objects) assigned to a station

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not all((char.isalnum() or char == "-") for char in value ):
            raise ValueError("Station names can contain only letters, numbers, and hyphens!")
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("A station cannot have a negative capacity!")
        self.__capacity = value

    def calculate_total_salaries(self):
        total_salaries = 0
        for astronaut in self.astronauts:
            total_salaries += astronaut.salary
        return f"{total_salaries:.2f}"

    def status(self):
        result1 = f"Station name: {self.name}; Astronauts: "
        result2 = ""
        if self.astronauts:
            sorted_astronauts = sorted(self.astronauts, key=lambda a: a.id_number)
            result2 = f"{' #'.join(a.id_number for a in sorted_astronauts)}"
        else:
            result2 = "N/A"
        total_result = result1 + result2 + "; Total salaries: " + self.calculate_total_salaries()
        return total_result

    @abstractmethod
    def update_salaries(self, min_value: float):
        pass










