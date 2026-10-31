from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    INITIAL_STRENGTH = 150
    NEED_STRENGTH = 75

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_STRENGTH)

    def can_climb(self) -> bool:
        return self.strength >= self.NEED_STRENGTH

    def climb(self, peak: BasePeak):
        if peak.difficulty_level == "Advanced":
            self.strength -= 30 * 1.3
        else:
            self.strength -= 30 * 2.5
        self.strength = max(self.strength, 0)
        self.strength = round(self.strength, 1)
        self.conquered_peaks.append(peak.name)


