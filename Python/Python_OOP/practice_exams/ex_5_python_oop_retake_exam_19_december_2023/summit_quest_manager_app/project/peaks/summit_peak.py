from project.peaks.base_peak import BasePeak


class SummitPeak(BasePeak):
    LEVEL_EXTREME = 2_500
    MIN_LEVEL_ADVANCED = 1_500
    MAX_LEVEL_ADVANCED = 2_500

    def __init__(self, name: str, elevation: int):
        super().__init__(name, elevation)
        self.difficulty_level: str = self.calculate_difficulty_level()

    def get_recommended_gear(self) -> list:
        return ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]

    def calculate_difficulty_level(self) -> str:
        if self.elevation > self.LEVEL_EXTREME:
            return "Extreme"

        if self.MIN_LEVEL_ADVANCED <= self.elevation <= self.MAX_LEVEL_ADVANCED:
            return "Advanced"


