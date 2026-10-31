from abc import ABC, abstractmethod
from math import floor
from project.equipment.base_equipment import BaseEquipment


class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name                #name of the team
        self.country = country          #country of origin of a team
        self.advantage = advantage      #the advantage in points that each team has
        self.budget = budget
        self.wins: int = 0              #value represents the team’s wins
        self.equipment: list[BaseEquipment] = []       #contain equipment(objects) each team has

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Team name cannot be empty!")
        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")
        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage = value

    @abstractmethod
    def win(self):#•	Increases the team’s advantage and the number of wins
        pass

    def get_statistics(self) -> str:
        avg_team_protection = floor(sum(p.protection for p in self.equipment)/len(self.equipment)) if self.equipment else 0
        result = [f"Name: {self.name}",
                  f"Country: {self.country}",
                  f"Advantage: {self.advantage} points",
                  f"Budget: {self.budget:.2f}EUR",
                  f"Wins: {self.wins}",
                  f"Total Equipment Price: {sum(e.price for e in self.equipment):.2f}",
                  f"Average Protection: {avg_team_protection}"]
        return '\n'.join(result)

