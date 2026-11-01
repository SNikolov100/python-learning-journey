from django.db.models import QuerySet, Count


class AuthorQuerySet(QuerySet):
    def get_authors_by_article_count(self):
        return self.annotate(
            number_articles=Count('article')
        ).order_by(
            '-number_articles',
            'email'
        )
