from project.astronauts.scientist_astronaut import ScientistAstronaut
from project.stations.base_station import BaseStation


class ResearchStation(BaseStation):
    INITIAL_CAPACITY = 5
    INCREASES_SALARY = 5_000
    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_CAPACITY)

    # def update_salaries(self, min_value: float):
    #     members_for_update = [a for a in self.astronauts if a.salary <= min_value]
    #     for member in members_for_update:
    #         member.salary += self.INCREASES_SALARY

    def update_salaries(self, min_value: float):
        members_for_update = [a for a in self.astronauts
                              if isinstance(a, ScientistAstronaut) and a.salary <= min_value]
        for member in members_for_update:
            member.salary += self.INCREASES_SALARY