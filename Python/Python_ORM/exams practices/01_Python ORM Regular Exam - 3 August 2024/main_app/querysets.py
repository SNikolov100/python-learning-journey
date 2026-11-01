from django.db.models import QuerySet, Count


class AstronautQuerySet(QuerySet):
    def by_missions_count(self):
        return self.annotate(count_missions=Count('missions')).order_by('-count_missions', 'phone_number')