from project.battleships.base_battleship import BaseBattleship
from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone
from project.zones.pirate_zone import PirateZone
from project.zones.royal_zone import RoyalZone


class BattleManager:
    valid_zones = {
        "RoyalZone": RoyalZone,
        "PirateZone": PirateZone,
    }

    valid_ships = {
        "RoyalBattleship": RoyalBattleship,
        "PirateBattleship": PirateBattleship
    }


    def __init__(self):
        self.zones: list[BaseZone] = []
        self.ships: list[BaseBattleship] = []

    def add_zone(self, zone_type: str, zone_code: str):
        if zone_type not in self.valid_zones:
            raise Exception("Invalid zone type!")

        zone_object = next((z for z in self.zones if z.code == zone_code), None)
        if zone_object:
            raise Exception("Zone already exists!")

        cls = self.valid_zones[zone_type](zone_code)
        self.zones.append(cls)
        return f"A zone of type {zone_type} was successfully added."

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        if ship_type not in self.valid_ships:
            raise Exception(f"{ship_type} is an invalid type of ship!")

        cls = self.valid_ships[ship_type](name, health, hit_strength)
        self.ships.append(cls)
        return f"A new {ship_type} was successfully added."

    @staticmethod
    def add_ship_to_zone(zone: BaseZone, ship: BaseBattleship):
        if zone.volume <= 0:
            return f"Zone {zone.code} does not allow more participants!"

        if ship.health <= 0 :
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"

        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"

        royal_type = (isinstance(zone, RoyalZone) and isinstance(ship, RoyalBattleship))
        pirate_type = (isinstance(zone, PirateZone) and isinstance(ship, PirateBattleship))

        if royal_type or pirate_type:
            ship.is_attacking = True
        else:
            ship.is_attacking = False

        zone.ships.append(ship)
        ship.is_available = False
        zone.volume -= 1
        return f"Ship {ship.name} successfully participated in zone {zone.code}."


    def remove_battleship(self, ship_name: str):
        ship_object = next((s for s in self.ships if s.name == ship_name), None)
        if ship_object is None:
            return "No ship with this name!"
        if not ship_object.is_available:
            return "The ship participates in zone battles! Removal is impossible!"
        self.ships.remove(ship_object)
        ship_object.is_available = True
        return f"Successfully removed ship {ship_name}."


    def start_battle(self, zone: BaseZone):
        target_ships = [ship for ship in zone.ships if not ship.is_attacking]
        attacker_ships = [ship for ship in zone.ships if ship.is_attacking]
        if not attacker_ships or not target_ships:
            return "Not enough participants. The battle is canceled."

        strongest_target_ship = max(target_ships, key=lambda t: t.health )
        strongest_attacker_ship = max(attacker_ships, key=lambda a: a.hit_strength)

        strongest_attacker_ship.attack()
        strongest_target_ship.take_damage(strongest_attacker_ship)

        if strongest_target_ship.health <= 0:
            zone.ships.remove(strongest_target_ship)
            self.ships.remove(strongest_target_ship)
            strongest_target_ship.is_available = True
            return f"{strongest_target_ship.name} lost the battle and was sunk."

        if strongest_attacker_ship.ammunition == 0:
            zone.ships.remove(strongest_attacker_ship)
            self.ships.remove(strongest_attacker_ship)
            strongest_attacker_ship.is_available = True
            return f"{strongest_attacker_ship.name} ran out of ammunition and leaves."

        return "Both ships survived the battle."

    def get_statistics(self):
        available_ships = [ship for ship in self.ships if ship.is_available]
        available_ships_count = len(available_ships)
        result = [f"Available Battleships: {available_ships_count}"]
        if available_ships:
            result.append("#" + ', '.join(ship.name for ship in available_ships) + "#")
        self.zones.sort(key=lambda z: z.code)
        result.append("***Zones Statistics:***")
        result.append(f"Total Zones: {len(self.zones)}")
        for zone in self.zones:
            result.append(zone.zone_info())
        return '\n'.join(result)









