from django.db.models import QuerySet, Count


class DirectorQuerySet(QuerySet):
    def get_directors_by_movies_count(self):
        return self.annotate(number_of_movies=Count('movie')).order_by('-number_of_movies', 'full_name')

