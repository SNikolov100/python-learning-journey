from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    INITIAL_OXYGEN = 540
    MISS_CATCH = 0.3
    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_OXYGEN)

    def miss(self, time_to_catch: int):
        reduced = round(self.MISS_CATCH * time_to_catch)
        if self.oxygen_level < reduced:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= reduced


    def renew_oxy(self):
        self.oxygen_level = self.INITIAL_OXYGEN

