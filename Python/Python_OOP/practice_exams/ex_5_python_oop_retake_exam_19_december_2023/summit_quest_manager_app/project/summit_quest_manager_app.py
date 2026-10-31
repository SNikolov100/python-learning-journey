from project.climbers.arctic_climber import ArcticClimber
from project.climbers.base_climber import BaseClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.base_peak import BasePeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    def __init__(self):
        self.climbers: list[BaseClimber] = []    #all climber objects registered for the Summit Quest
        self.peaks: list[BasePeak] = []          #all peak objects that are part of the wish list to climb.

    def register_climber(self, climber_type: str, climber_name: str):
        valid_types_of_climbers = {"ArcticClimber": ArcticClimber,
                                   "SummitClimber": SummitClimber}
        if climber_type not in valid_types_of_climbers.keys():
            return f"{climber_type} doesn't exist in our register."

        for c in self.climbers:
            if c.name == climber_name:
                return f"{climber_name} has been already registered."

        cls_climber = valid_types_of_climbers[climber_type](climber_name)
        self.climbers.append(cls_climber)
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        valid_peaks = {"ArcticPeak": ArcticPeak,
                       "SummitPeak": SummitPeak}
        if peak_type not in valid_peaks:
            return f"{peak_type} is an unknown type of peak."
        cls_peak = valid_peaks[peak_type](peak_name, peak_elevation)
        self.peaks.append(cls_peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: list[str]):
        climber_object = next((c for c in self.climbers if c.name == climber_name), None)
        peak_object = next((p for p in self.peaks if p.name == peak_name), None)
        if climber_object is not None and peak_object is not None:

            need_gears = peak_object.get_recommended_gear()
            missing_gears = []
            for tool in need_gears:
                if tool not in gear:
                    missing_gears.append(tool)

            if missing_gears:
                climber_object.is_prepared = False
                sorted_missing_gears = sorted(missing_gears, key=lambda x: x)
                return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sorted_missing_gears)}."

            climber_object.is_prepared = True
            return f"{climber_name} is prepared to climb {peak_name}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        climber_object = next((c for c in self.climbers if c.name == climber_name), None)
        peak_object = next((p for p in self.peaks if p.name == peak_name), None)

        if climber_object is None:
            return f"Climber {climber_name} is not registered yet."
        if peak_object is None:
            return f"Peak {peak_name} is not part of the wish list."

        if climber_object.is_prepared and climber_object.can_climb():
            climber_object.climb(peak_object)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak_object.difficulty_level}."
        elif not climber_object.is_prepared:
            return f"{climber_name} will need to be better prepared next time."

        climber_object.rest()
        return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):
        success_climbers = [c for c in self.climbers if c.conquered_peaks]
        if success_climbers:
            sorted_success_climbers = sorted(success_climbers,key=lambda x: (-len(x.conquered_peaks), x.name))
            all_peaks = []

            for c in success_climbers:
                all_peaks.extend(c.conquered_peaks)

            conquered_peaks = set(p for p in all_peaks)

            result = [f"Total climbed peaks: {len(conquered_peaks)}",
                      f"**Climber's statistics:**",
                      ]
            for climb_peak in sorted_success_climbers:
                climb_peak.conquered_peaks = sorted(climb_peak.conquered_peaks)
                result.append(f"{str(climb_peak)}")
            return '\n'.join(result)



