from abc import ABC, abstractmethod

from project.fish.base_fish import BaseFish


class BaseDiver(ABC):
    def __init__(self, name: str, oxygen_level: float):
        self.name = name                            #name of the diver
        self.oxygen_level = oxygen_level            #diver's oxygen level remaining, in seconds
        self.catch: list[BaseFish] = []                       #store a sequence of fish, caught by a specific diver
        self.competition_points: float = 0.0          #total points accumulated by a diver, based on the type of fish caught during the competition
        self.has_health_issue: bool = False         #False, representing that the diver starts in a healthy state

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Diver name cannot be null or empty!")
        self.__name = value

    @property
    def oxygen_level(self):
        return self.__oxygen_level

    @oxygen_level.setter
    def oxygen_level(self, value):
        if value < 0:
            raise ValueError("Cannot create diver with negative oxygen level!")
        self.__oxygen_level = value

    @property
    def competition_points(self):
        return self.__competition_points

    @competition_points.setter
    def competition_points(self, value : float):
        self.__competition_points = round(value, 1)

    @abstractmethod
    def miss(self, time_to_catch: int):
        pass

    @abstractmethod
    def renew_oxy(self):
        pass

    def hit(self, fish: BaseFish):
        self.oxygen_level -= fish.time_to_catch
        if self.oxygen_level < 0:
            self.oxygen_level = 0
        else:
            self.catch.append(fish)
            self.competition_points += round(fish.points, 1)

    def update_health_status(self):
        self.has_health_issue = not self.has_health_issue

    def __str__(self):
        return f"{self.__class__.__name__}: [Name: {self.name}, Oxygen level left: {self.oxygen_level}, Fish caught: {len(self.catch)}, Points earned: {self.competition_points:.1f}]"


