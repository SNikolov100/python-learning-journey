from django.db.models import QuerySet, Count


class ProfileQuerySet(QuerySet):
    def get_regular_customers(self) ->QuerySet:
        return (self.annotate(number_of_orders=Count('order', distinct=True))
                .filter(number_of_orders__gt=2)
                .order_by('-number_of_orders'))

