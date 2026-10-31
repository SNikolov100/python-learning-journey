from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):
    @property
    def allow_food(self) -> list:
        return [Meat]

    @property
    def wight_increase(self) -> float:
        return 0.25

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

class Hen(Bird):
    @property
    def allow_food(self) ->list:
        return [Vegetable, Fruit, Meat, Seed]

    @property
    def wight_increase(self) -> float:
        return 0.35

    @staticmethod
    def make_sound():
        return "Cluck"


