from project.battleships.pirate_battleship import PirateBattleship
from project.zones.base_zone import BaseZone


class RoyalZone(BaseZone):
    INITIAL_VOLUME = 10

    def __init__(self, code: str):
        super().__init__(code, self.INITIAL_VOLUME)
        self.zone_type = "RoyalZone"

    def zone_info(self):
        pirate_ships = sum(1 for ship in self.ships if isinstance(ship, PirateBattleship))

        result = ["@Royal Zone Statistics@",
                  f"Code: {self.code}; Volume: {self.volume}",
                  f"Battleships currently in the Royal Zone: {len(self.ships)}, {pirate_ships} out of them are Pirate Battleships."
                  ]
        ships = self.get_ships()
        if ships:
            result_2 = ', '.join(ship.name for ship in ships)
            result_2 = "#" + result_2 + "#"
            result.append(result_2)
        return '\n'.join(result)


