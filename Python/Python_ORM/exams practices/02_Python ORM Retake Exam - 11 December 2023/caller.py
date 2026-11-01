import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import TennisPlayer, Match, Tournament
from django.db.models import Q, Count


# Create queries within functions
def get_tennis_players(search_name=None, search_country=None) ->str:
    if search_name is None and search_country is None:
        return ""

    if search_name is None:
        tennis_objects=TennisPlayer.objects.filter(
            country__icontains=search_country
        ).order_by('ranking')

    elif search_country is None:
        tennis_objects = TennisPlayer.objects.filter(
            full_name__icontains=search_name
        ).order_by('ranking')

    else:
        tennis_objects = TennisPlayer.objects.filter(
        full_name__icontains= search_name,
        country__icontains= search_country
    ).order_by('ranking')

    if not tennis_objects:
        return ""

    return '\n'.join(f"Tennis Player: {to.full_name}, country: {to.country}, ranking: {to.ranking}" for to in tennis_objects)


def get_top_tennis_player() ->str:
    tennis_object = (TennisPlayer.objects.annotate(
        num_of_wins= Count('winner_matches')
        ).order_by('-num_of_wins', 'full_name').first()
    )
    if tennis_object is None:
        return ""
    return f"Top Tennis Player: {tennis_object.full_name} with {tennis_object.num_of_wins} wins."

def get_tennis_player_by_matches_count() ->str:
    tennis_object = (TennisPlayer.objects
        .annotate(num_of_matches=Count('players_matches'))
        .order_by('-num_of_matches', 'ranking')
        .first()
    )
    if tennis_object is None or tennis_object.num_of_matches == 0:
        return ""
    return f"Tennis Player: {tennis_object.full_name} with {tennis_object.num_of_matches} matches played."


def get_tournaments_by_surface_type(surface=None) -> str:
    if surface is None:
        return ""

    tournament_objects = (Tournament.objects
                            .filter(surface_type__icontains=surface)
                            .annotate(num_matches=Count('tournament_matches'))
                            .order_by('-start_date')
                          )

    if not tournament_objects.exists():
        return ""

    return '\n'.join(f"Tournament: {to.name}, start date: {to.start_date}, matches: {to.num_matches}" for to in tournament_objects)


def get_latest_match_info() ->str:
    last_match = (Match.objects
                  .select_related('tournament', 'winner')
                  .prefetch_related('players')
                  .order_by('-date_played','-id')
                  .first()
                  )

    if last_match is None:
        return ""

    player1, player2 = last_match.players.all().order_by('full_name')

    if last_match.winner is None:
        winner = 'TBA'
    else:
        winner = last_match.winner.full_name

    return (f"Latest match played on: {last_match.date_played}"
            f", tournament: {last_match.tournament.name}"
            f", score: {last_match.score}"
            f", players: {player1.full_name} vs {player2.full_name}"
            f", winner: {winner}, summary: {last_match.summary}")



def get_matches_by_tournament(tournament_name=None):
    matches_objects = (Match.objects
                       .select_related('tournament', 'winner')
                       .filter(tournament__name__exact=tournament_name)
                       .order_by('-date_played')
                       )
    if not matches_objects.exists() or tournament_name is None:
        return "No matches found."

    return '\n'.join(f"Match played on: {mo.date_played},"
                     f" score: {mo.score},"
                     f" winner: {'TBA' if mo.winner is None else mo.winner.full_name}"
                     for mo in matches_objects)












