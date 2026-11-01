import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Article, Review
# Import your models here
from django.db.models import Count, Avg, Prefetch


# Create queries within functions
def get_authors(search_name=None, search_email=None) ->str:
    if search_name is None and search_email is None:
        return ""

    elif search_name is None and search_email is not None:
        author_objects =(Author.objects
            .filter(email__icontains=search_email)
            .order_by('-full_name')
        )

    elif search_name is not None and search_email is None:
        author_objects=(Author.objects
                        .filter(full_name__icontains=search_name)
                        .order_by('-full_name')
                        )
    else:
        author_objects=(Author.objects
                        .filter(full_name__icontains=search_name, email__icontains=search_email)
                        .order_by('-full_name')
                        )

    return '\n'.join(f"Author: {a.full_name}, email: {a.email},"
                     f" status: {'Banned' if a.is_banned else 'Not Banned'}" for a in author_objects)

def get_top_publisher():
    author_object = (Author.objects
                     .annotate(num_of_articles=Count('article'))
                     .filter(num_of_articles__gt=0)
                     .order_by('-num_of_articles', 'email')
                     .first()
                     )

    if author_object is None:
        return ""

    return f"Top Author: {author_object.full_name} with {author_object.num_of_articles} published articles."


def get_top_reviewer() ->str:
    author_object = (Author.objects
                     .annotate(num_of_reviews=Count('review'))
                     .filter(num_of_reviews__gt=0)
                     .order_by('-num_of_reviews', 'email')
                     .first()
                     )
    if author_object is None:
        return ""

    return f"Top Reviewer: {author_object.full_name} with {author_object.num_of_reviews} published reviews."

def get_latest_article() ->str:
    article_object = (Article.objects
                      .prefetch_related(Prefetch('authors', queryset=Author.objects.order_by('full_name')))
                      .annotate(num_reviews=Count('review'), avg_reviews_rating=Avg('review__rating'))
                      .order_by('published_on')
                      .last()
                      )
    if article_object is None:
        return ""

    return (f"The latest article is: {article_object.title}."
            f" Authors: {', '.join(a.full_name for a in article_object.authors.all())}"
            f" Reviewed: {article_object.num_reviews} times."
            f" Average Rating: {article_object.avg_reviews_rating:.2f}.")


def get_top_rated_article() ->str:
    article_object= (Article.objects
                     .annotate(
        num_reviews=Count('review'),
        avg_rating=Avg('review__rating')
                     )
                     .filter(num_reviews__gt=0)
                     .order_by('-avg_rating','title')
                     .first()
    )
    if article_object is None:
        return ""

    return (f"The top-rated article is: {article_object.title}, with an average rating of {article_object.avg_rating}:.2f,"
            f" reviewed {article_object.num_reviews} times.")

def ban_author(email=None) ->str:
    if email is None:
        return "No authors banned."
    author_object = (Author.objects
                     .filter(email=email)
                     .first()
                     )
    if author_object is None:
        return "No authors banned."

    author_object.is_banned=True
    author_object.save()
    num_reviews = author_object.review_set.all().delete()[0]
    result = f"Author: {author_object.full_name} is banned! {num_reviews} reviews deleted."
    return result
