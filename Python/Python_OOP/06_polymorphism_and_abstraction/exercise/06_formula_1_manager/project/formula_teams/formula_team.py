from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    MIN_BUDGET = 1_000_000
    def __init__(self, budget:int):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if isinstance(value, int):
            if value < FormulaTeam.MIN_BUDGET:
                raise ValueError("F1 is an expensive sport, find more sponsors!")
            self.__budget = value

    @abstractmethod
    def revenue__per_race(self) -> dict[str, dict[int, int]]:
        pass

    @abstractmethod
    def expenses_per_race(self) -> int:
        pass

    def calculate_revenue_after_race(self, race_position: int) -> str:
        revenue = 0
        for data in self.revenue__per_race().values():
            for position, profit in data.items():
                if race_position <= position:
                    revenue += profit
                    break
        revenue -= self.expenses_per_race()
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"

