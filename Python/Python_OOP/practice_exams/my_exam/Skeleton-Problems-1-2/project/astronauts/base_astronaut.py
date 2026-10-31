from abc import ABC, abstractmethod


class BaseAstronaut(ABC):
    def __init__(self, id_number: str, salary: float, specialization: str, stamina: int):
        self.id_number = id_number              #identity number (ID) of the astronaut.
        self.salary = salary                    #salary of the astronaut.
        self.specialization = specialization    #specialization of the astronaut
        self.stamina = stamina                  #energy level of the astronaut

    @property
    def id_number(self):
        return self.__id_number

    @id_number.setter
    def id_number(self, value):
        if not all(ch.isdigit() for ch in value ):
            raise ValueError("ID can contain only digits!")
        self.__id_number = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary must be a positive number!")
        self.__salary = value

    @property
    def specialization(self):
        return self.__specialization

    @specialization.setter
    def specialization(self, value):
        if value.strip() == "":
            raise ValueError("Specialization cannot be empty!")
        self.__specialization = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value < 0 or value > 100:
            raise ValueError("Stamina is out of range!")
        self.__stamina = value

    @abstractmethod
    def train(self):
        pass

    @property
    @abstractmethod
    def type_astronaut(self):
        pass

