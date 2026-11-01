from django.db.models import QuerySet
from django.db.models.aggregates import Count


class AstronautQuerySet(QuerySet):
    def get_astronauts_by_missions_count(self):
        return (self
                .annotate(number_of_missions=Count('mission'))
                .order_by('-number_of_missions', 'phone_number')
                )

