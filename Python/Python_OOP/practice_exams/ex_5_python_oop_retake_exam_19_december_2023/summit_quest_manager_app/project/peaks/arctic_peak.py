from project.peaks.base_peak import BasePeak


class ArcticPeak(BasePeak):
    LEVEL_EXTREME = 3_000
    MIN_LEVEL_ADVANCED = 2_000
    MAX_LEVEL_ADVANCED = 3_000

    def __init__(self, name: str, elevation: int):
        super().__init__(name, elevation)
        self.difficulty_level: str = self.calculate_difficulty_level()

    def get_recommended_gear(self) -> list:
        return ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]

    def calculate_difficulty_level(self) -> str:
        if self.elevation > self.LEVEL_EXTREME:
            return "Extreme"
        if self.MIN_LEVEL_ADVANCED <= self.elevation <= self.MAX_LEVEL_ADVANCED:
            return "Advanced"

