import os
import django
from sqlparse.sql import Case

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()
from main_app.models import Director, Actor, Movie
from main_app.populate_db import populate_model_with_data
from django.db.models import Count, Avg, F


# Import your models here

# Create queries within functions
def populate_db():
    populate_model_with_data(Director)
    populate_model_with_data(Actor)
    populate_model_with_data(Movie)


def get_directors(search_name=None, search_nationality=None) ->str:
    if search_name is not None and search_nationality is not None:
        director_objects = (Director.objects
                            .filter(full_name__icontains=search_name,
                                    nationality__icontains=search_nationality
                                    )
                            .order_by('full_name')
                            )
    elif search_name is not None:
        director_objects = (Director.objects
                            .filter(full_name__icontains=search_name)
                            .order_by('full_name')
                            )
    elif search_nationality is not None:
        director_objects = (Director.objects
                            .filter(nationality__icontains=search_nationality)
                            .order_by('full_name')
                            )
    else:
        return ""
    if not director_objects.exists():
        return ""

    return '\n'.join(f"Director: {d.full_name},"
                     f" nationality: { d.nationality},"
                     f" experience: {d.years_of_experience}"
                     for d in director_objects)

def get_top_director():
    director_object = Director.objects.get_directors_by_movies_count().first()
    if director_object is None:
        return ""
    return f"Top Director: {director_object.full_name}, movies: {director_object.number_of_movies}."

def get_top_actor():
    starring_actor = (Actor.objects
                      .prefetch_related('movie_set')
                      .annotate(num_of_movies=Count('movie'),
                                movies_avg_rating=Avg('movie__rating')
                                )
                      .filter(num_of_movies__gt=0)
                      .order_by('-num_of_movies', 'full_name')
                      .first()
                      )
    if starring_actor is None:
        return ""
    titles = []
    for movie in starring_actor.movie_set.all():
        titles.append(movie.title)

    return (f"Top Actor: {starring_actor.full_name},"
            f" starring in movies: {', '.join(titles)},"
            f" movies average rating: {starring_actor.movies_avg_rating:.1f}")


def get_actors_by_movies_count():
    top_three_actors = (Actor.objects
                        .annotate(count_movies=Count('movies'))
                        .filter(count_movies__gt=0)
                        .order_by('-count_movies', 'full_name')
                        )[:3]
    if not top_three_actors.exists():
        return ""
    result = []
    for actor in top_three_actors:
        result.append(f"{actor.full_name}, participated in {actor.count_movies} movies")
    return '\n'.join(result)


def get_top_rated_awarded_movie():
    high_rating_movie = (Movie.objects
                         .prefetch_related('actors')
                         .select_related('starring_actor')
                         .filter(is_awarded=True)
                         .order_by('-rating', 'title', )
                         .first()
                         )
    if high_rating_movie is None:
        return ""

    starring_actor_full_name = 'N/A' if high_rating_movie.starring_actor.full_name is None else high_rating_movie.starring_actor.full_name
    return (f"Top rated awarded movie: {high_rating_movie.title},"
            f" rating: {high_rating_movie.rating}."
            f" Starring actor: {starring_actor_full_name}."
            f" Cast: " + ', '.join(a.full_name for a in high_rating_movie.actors.all().order_by('full_name') )
            )


def increase_rating() ->str:
    num_of_updated_movies = (Movie.objects
                      .filter(is_classic=True, rating__lt=10.0)
                      .update(rating=F('rating') + 0.1)
                      )
    if num_of_updated_movies == 0:
        return "No ratings increased."

    return f"Rating increased for {num_of_updated_movies} movies."

