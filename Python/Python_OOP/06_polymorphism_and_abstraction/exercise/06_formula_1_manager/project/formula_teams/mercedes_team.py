from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    SPONSORS = {"Petronas":{1: 1_000_000,
                          3: 500_000},
                "TeamViewer":{5: 100_000,
                         7: 50_000}}
    EXPENSES_PER_RACE = 200_000

    def expenses_per_race(self) -> int:
        return MercedesTeam.EXPENSES_PER_RACE

    def revenue__per_race(self) -> dict[str, dict[int, int]]:
        return MercedesTeam.SPONSORS