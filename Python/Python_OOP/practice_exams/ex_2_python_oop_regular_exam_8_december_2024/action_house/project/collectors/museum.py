from project.collectors.base_collector import BaseCollector


class Museum(BaseCollector):
    INITIAL_MONEY = 15_000.00
    INITIAL_SPACE = 2_000
    def __init__(self, name: str):
        super().__init__(name, Museum.INITIAL_MONEY, Museum.INITIAL_SPACE)

    def increase_money(self):
        self.available_money += 1_000.00
        return self.available_money

