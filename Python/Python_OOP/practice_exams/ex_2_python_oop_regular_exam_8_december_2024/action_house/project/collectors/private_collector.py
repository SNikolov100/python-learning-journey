from project.collectors.base_collector import BaseCollector


class PrivateCollector(BaseCollector):
    INITIAL_MONEY = 25_000.00
    INITIAL_SPACE = 3_000

    def __init__(self, name: str):
        super().__init__(name, PrivateCollector.INITIAL_MONEY, PrivateCollector.INITIAL_SPACE)

    def increase_money(self):
        self.available_money += 5_000.00
        return self.available_money

