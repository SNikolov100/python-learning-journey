from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    SPONSORS = {"Oracle":{1: 1_500_000,
                          2: 800_000},
                "Honda":{8: 20_000,
                         10: 10_000}}
    EXPENSES_PER_RACE = 250_000

    def expenses_per_race(self) -> int:
        return RedBullTeam.EXPENSES_PER_RACE

    def revenue__per_race(self) -> dict[str, dict[int, int]]:
        return RedBullTeam.SPONSORS
