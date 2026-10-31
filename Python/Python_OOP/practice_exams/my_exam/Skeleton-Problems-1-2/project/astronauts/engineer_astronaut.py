from project.astronauts.base_astronaut import BaseAstronaut


class EngineerAstronaut(BaseAstronaut):
    INITIAL_STAMINA = 80
    SPECIALISATION = "EngineerAstronaut"
    INCREASE_STAMINA = 5
    def __init__(self, id_number: str, salary: float):
        super().__init__(id_number, salary, self.SPECIALISATION, self.INITIAL_STAMINA)

    def train(self):
        if (self.stamina + self.INCREASE_STAMINA) >= 100:
            self.stamina = 100
        else:
            self.stamina += self.INCREASE_STAMINA

    @property
    def type_astronaut(self):
        return self.SPECIALISATION
