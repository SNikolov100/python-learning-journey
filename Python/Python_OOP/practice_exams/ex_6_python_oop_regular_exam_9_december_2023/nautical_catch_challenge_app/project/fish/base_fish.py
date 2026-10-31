from abc import ABC, abstractmethod


class BaseFish(ABC):
    def __init__(self, name: str, points: float, time_to_catch: int):
        self.name = name                    #name of the fish
        self.points = points                #points a fish will bring to the diver
        self.time_to_catch = time_to_catch  #how many seconds a diver requires to catch the fish
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Fish name should be determined!")
        self.__name = value

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, value: float):
        if not 1.0 <= value <= 10.0:
            raise ValueError("Points should be a value ranging from 1 to 10!")
        self.__points = value

    @abstractmethod
    def fish_details(self) -> str:    #•	Returns a string with information about the fish depending on its type.
        pass


