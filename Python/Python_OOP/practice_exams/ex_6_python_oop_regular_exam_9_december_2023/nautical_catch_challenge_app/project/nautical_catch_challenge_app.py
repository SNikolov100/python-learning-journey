from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    def __init__(self):
        self.divers: list[BaseDiver] = []        #store all diver objects assigned for the competition
        self.fish_list: list[BaseFish] = []     #storing all fish objects that are allowed for chasing in the competition

    def dive_into_competition(self, diver_type: str, diver_name: str):
        valid_type_divers = {"FreeDiver": FreeDiver,
                        "ScubaDiver": ScubaDiver}
        if diver_type not in valid_type_divers:
            return f"{diver_type} is not allowed in our competition."

        diver_object = next((d for d in self.divers if d.name == diver_name), None)
        if diver_object:
            return f"{diver_name} is already a participant."
        cls_diver = valid_type_divers[diver_type](diver_name)
        self.divers.append(cls_diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        valid_type_fish = {"PredatoryFish": PredatoryFish,
                           "DeepSeaFish": DeepSeaFish}
        if fish_type not in valid_type_fish:
            return f"{fish_type} is forbidden for chasing in our competition."

        fish_object = next((f for f in self.fish_list if f.name == fish_name), None)
        if fish_object:
            return f"{fish_name} is already permitted."

        cls_fish = valid_type_fish[fish_type](fish_name, points)
        self.fish_list.append(cls_fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver_object = next((d for d in self.divers if d.name == diver_name), None)
        fish_object = next((f for f in self.fish_list if f.name == fish_name), None)

        if diver_object is None:
            return f"{diver_name} is not registered for the competition."

        if fish_object is None:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver_object.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver_object.oxygen_level < fish_object.time_to_catch:
            diver_object.oxygen_level = 0
            diver_object.update_health_status()
            return f"{diver_name} missed a good {fish_name}."

        if diver_object.oxygen_level == fish_object.time_to_catch:
            if is_lucky:
                diver_object.hit(fish_object)
                diver_object.update_health_status()
                return f"{diver_name} hits a {fish_object.points}pt. {fish_name}."

            diver_object.miss(fish_object.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."

        diver_object.hit(fish_object)
        return f"{diver_name} hits a {fish_object.points:.1f}pt. {fish_name}."

    def health_recovery(self):
        count = 0
        divers_with_issue = [d for d in self.divers if d.has_health_issue]
        if divers_with_issue:
            for diver in divers_with_issue:
                diver.update_health_status()
                diver.renew_oxy()
                count += 1
        return f"Divers recovered: {count}"

    def diver_catch_report(self, diver_name: str):
        diver_object = next((d for d in self.divers if d.name == diver_name), None)

        result = [f"**{diver_name} Catch Report**"]
        for fish in diver_object.catch:
            result.append(fish.fish_details())
        return "\n".join(result)

    def competition_statistics(self):
        diver_in_good_condition = [d for d in self.divers if not d.has_health_issue]
        sorted_diver_in_good_condition = sorted(diver_in_good_condition, key=lambda d: (-d.competition_points, -len(d.catch), d.name))
        result = [f"**Nautical Catch Challenge Statistics**"]
        for diver in sorted_diver_in_good_condition:
            result.append(str(diver))
        return "\n".join(result)








