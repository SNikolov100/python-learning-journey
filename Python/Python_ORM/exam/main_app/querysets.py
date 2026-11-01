from django.db.models import QuerySet, Count


class PublisherQuerySet(QuerySet):
    def get_publishers_by_books_count(self):
        return self.annotate(num_books=Count('book')).order_by('-num_books', 'name')