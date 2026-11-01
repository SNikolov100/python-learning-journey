from django.db.models import Manager
from main_app.querysets import TennisPlayerQuerySet


class TennisPlayerManager(Manager.from_queryset(TennisPlayerQuerySet)):
    def get_tennis_players_by_wins_count(self):
        return self.tennis_player_wins_order()