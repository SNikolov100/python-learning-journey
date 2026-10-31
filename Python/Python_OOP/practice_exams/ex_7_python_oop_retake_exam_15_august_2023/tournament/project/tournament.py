from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    def __init__(self, name: str, capacity: int):
        self.name = name            #name of the tournament
        self.capacity = capacity    #o	The number of teams а Tournament can have.
        self.equipment: list[BaseEquipment] = []    #contain all equipment (objects) that are created.
        self.teams: list[BaseTeam] = []             #contain all teams (objects) that are created

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        valid_type_equipment = {"KneePad": KneePad,
                                "ElbowPad": ElbowPad}

        if equipment_type not in valid_type_equipment:
            raise Exception("Invalid equipment type!")

        cls_equipment = valid_type_equipment[equipment_type]()
        self.equipment.append(cls_equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        valid_type_teams = {"OutdoorTeam": OutdoorTeam,
                            "IndoorTeam": IndoorTeam}

        if team_type not in valid_type_teams:
            raise Exception("Invalid team type!")

        if self.capacity <= len(self.teams):
            return "Not enough tournament capacity."

        cls_team = valid_type_teams[team_type](team_name, country, advantage)
        self.teams.append(cls_team)

        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        team_object = next((t for t in self.teams if t.name == team_name), None)
        equipment_objects = [e for e in self.equipment if e.__class__.__name__ == equipment_type]

        equipment_object = equipment_objects.pop()
        if team_object.budget < equipment_object.price:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equipment_object)
        team_object.equipment.append(equipment_object)
        team_object.budget -= equipment_object.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team_object = next((t for t in self.teams if t.name == team_name), None)
        if team_object is None:
            raise Exception("No such team!")

        if team_object.wins > 0:
            raise Exception(f"The team has {team_object.wins} wins! Removal is impossible!")

        self.teams.remove(team_object)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        equipment_objects = [e for e in self.equipment if e.__class__.__name__ == equipment_type]
        for equipment in equipment_objects:
            equipment.increase_price()

        return f"Successfully changed {len(equipment_objects)}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team_1 = next((t for t in self.teams if t.name == team_name1),None)
        team_2 = next((t for t in self.teams if t.name == team_name2),None)
        if type(team_1) != type(team_2):
            raise Exception("Game cannot start! Team types mismatch!")

        all_protection_team_1 = sum(p.protection for p in team_1.equipment)
        sum_points_team_1 = team_1.advantage + all_protection_team_1

        all_protection_team_2 = sum(p.protection for p in team_2.equipment)
        sum_points_team_2 = team_2.advantage + all_protection_team_2

        if sum_points_team_1 > sum_points_team_2:
            team_1.win()
            return f"The winner is {team_1.name}."

        if sum_points_team_2 > sum_points_team_1:
            team_2.win()
            return f"The winner is {team_2.name}."

        return f"No winner in this game."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda t: -t.wins)
        result = [f"Tournament: {self.name}",
                  f"Number of Teams: {len(self.teams)}",
                  "Teams:"]

        for team in sorted_teams:
            result.append(team.get_statistics())

        return '\n'.join(result)


