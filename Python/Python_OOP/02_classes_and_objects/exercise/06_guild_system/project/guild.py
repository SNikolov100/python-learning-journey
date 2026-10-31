from project.player import Player

class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players:list[Player] = []

    def assign_player(self, player: Player) -> str:
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        if player.guild != Player.NO_GUILD:
            return f"Player {player.name} is in another guild."
        self.players.append(player)
        player.guild = self.name
        return  f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str) -> str:
        player = next((p for p in self.players if p.name == player_name), None)
        if not player:
            return f"Player {player_name} is not in the guild."
        self.players.remove(player)
        player.guild = Player.NO_GUILD
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self) -> str:
        result = [f"Guild: {self.name}"]
        for player in self.players:
            result.append(player.player_info())
        return "\n".join(result)





