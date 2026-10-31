from project.astronauts.base_astronaut import BaseAstronaut
from project.astronauts.engineer_astronaut import EngineerAstronaut
from project.astronauts.scientist_astronaut import ScientistAstronaut
from project.stations.base_station import BaseStation
from project.stations.maintenance_station import MaintenanceStation
from project.stations.research_station import ResearchStation


class SpaceAgency:
    def __init__(self):
        self.astronauts: list[BaseAstronaut] = []       #all astronaut objects available for assignments
        self.stations: list[BaseStation] = []           #all station objects owned by the agency

    def add_astronaut(self, astronaut_type: str, astronaut_id_number: str, astronaut_salary: float):
        valid_astr_type = {"EngineerAstronaut": EngineerAstronaut,
                           "ScientistAstronaut": ScientistAstronaut}
        if astronaut_type not in valid_astr_type:
            raise ValueError("Invalid astronaut type!")

        if any(a for a in self.astronauts if a.id_number == astronaut_id_number):
            raise ValueError(f"{astronaut_id_number} has been already added!")

        cls_astr = valid_astr_type[astronaut_type](astronaut_id_number, astronaut_salary)
        self.astronauts.append(cls_astr)
        return f"{astronaut_id_number} is successfully hired as {astronaut_type}."

    def add_station(self, station_type: str, station_name: str):
        valid_station_type = {"ResearchStation": ResearchStation,
                              "MaintenanceStation": MaintenanceStation}
        if station_type not in valid_station_type:
            raise ValueError("Invalid station type!")

        if any(s for s in self.stations if s.name == station_name):
            raise ValueError(f"{station_name} has been already added!")

        cls_station = valid_station_type[station_type](station_name)
        self.stations.append(cls_station)
        return f"{station_name} is successfully added as a {station_type}."

    def assign_astronaut(self, station_name: str, astronaut_type: str):
        station_obj = next((s for s in self.stations if s.name == station_name), None)
        if station_obj is None:
            raise ValueError(f"Station {station_name} does not exist!")

        astr_obj = next ((a for a in self.astronauts if a.type_astronaut == astronaut_type), None)
        if astr_obj is None:
            raise ValueError("No available astronauts of the type!")

        if station_obj.capacity <= 0:
            return f"This station has no available capacity."

        self.astronauts.remove(astr_obj)
        station_obj.astronauts.append(astr_obj)
        station_obj.capacity -= 1
        return f"{astr_obj.id_number} was assigned to {station_obj.name}."

    def train_astronauts(self, station: BaseStation, sessions_number: int):
        for _ in range(sessions_number):
            for astronaut in station.astronauts:
                astronaut.train()
        total_stamina = 0
        for astronaut in station.astronauts:
            total_stamina += astronaut.stamina
        result = f"{station.name} astronauts have {total_stamina} total stamina after {sessions_number} training session/s."
        return result

    def retire_astronaut(self, station: BaseStation, astronaut_id_number: str):
        astr_obj = next((a for a in station.astronauts if a.id_number == astronaut_id_number), None)
        if  astr_obj is None or astr_obj.stamina == 100:
            return "The retirement process was canceled."

        station.astronauts.remove(astr_obj)
        station.capacity += 1
        return f"Retired astronaut {astronaut_id_number}."

    def agency_update(self, min_value: float):
        for station in self.stations:
            station.update_salaries(min_value)

        available_astronauts_count = len(self.astronauts)
        stations_total_count = len(self.stations)
        total_available_capacity = sum(s.capacity for s in self.stations)
        sorted_stations = sorted(self.stations, key=lambda s: (-len(s.astronauts), s.name))

        result = ["*Space Agency Up-to-Date Report*",
                  f"Total number of available astronauts: {available_astronauts_count}",
                  f"**Stations count: {stations_total_count}; Total available capacity: {total_available_capacity}**"]

        for station in sorted_stations:

            result.append(station.status())

        return "\n".join(result)












