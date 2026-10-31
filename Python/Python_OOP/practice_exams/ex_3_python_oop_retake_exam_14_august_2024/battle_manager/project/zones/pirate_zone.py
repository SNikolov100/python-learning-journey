from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):
    INITIAL_VOLUME = 8
    def __init__(self, code: str):
        super().__init__(code, self.INITIAL_VOLUME)
        self.zone_type = "PirateZone"

    def zone_info(self):
        royal_ships = sum(1 for ship in self.ships if isinstance(ship, RoyalBattleship))

        result = ["@Pirate Zone Statistics@",
                  f"Code: {self.code}; Volume: {self.volume}",
                  f"Battleships currently in the Pirate Zone: {len(self.ships)}, {royal_ships} out of them are Royal Battleships."
                  ]
        ships = self.get_ships()
        if ships:
            result_2 = ', '.join(ship.name for ship in ships)
            result_2 = "#" + result_2 + "#"
            result.append(result_2)
        return '\n'.join(result)

