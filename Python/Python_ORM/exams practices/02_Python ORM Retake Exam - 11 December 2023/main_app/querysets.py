from django.db.models import QuerySet, Count

class TennisPlayerQuerySet(QuerySet):
    def tennis_player_wins_order(self):
        return self.annotate(count_win_matches= Count('winner_matches')).order_by('-count_win_matches', 'full_name')