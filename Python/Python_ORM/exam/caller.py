import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Publisher, Author, Book
from main_app.populate_db import populate_model_with_data
from django.db.models import Q, Count, Avg, Sum, F, Case, When, ExpressionWrapper, DecimalField


# Create queries within functions
def populate_db():
    populate_model_with_data(Publisher)
    populate_model_with_data(Author)
    populate_model_with_data(Book)

def get_publishers(search_string=None) ->str:
    if search_string is None:
        return "No search criteria."

    find_objects = (Publisher.objects
                    .filter(Q(name__icontains=search_string)
                            |
                            Q(country__icontains=search_string)
                            )
                    .order_by('-rating', 'name')
                    )
    if not find_objects.exists():
        return 'No publishers found.'

    return '\n'.join(f"Publisher: {p.name},"
                     f" country: {'Unknown' if p.country == 'TBC' else p.country},"
                     f" rating: {p.rating:.1f}" for p in find_objects.all())


def get_top_publisher() ->str:
    top_publisher = Publisher.objects.get_publishers_by_books_count().first()
    if top_publisher is None:
        return "No publishers found."
    return f"Top Publisher: {top_publisher.name} with {top_publisher.num_books} books."

def get_top_main_author() ->str:
    top_author = (Author.objects
                  .prefetch_related('book_set')
                  .annotate(num_main_books=Count('book'), books_avg_rating=Avg('book__rating'))
                  .filter(num_main_books__gt=0)
                  .order_by('-num_main_books', 'name')
                  .first()
                  )
    if top_author is None:
        return "No results."
    books_avg_rating = top_author.books_avg_rating
    return (f"Top Author: {top_author.name},"
            f" own book titles: {', '.join(a.title for a in top_author.book_set.order_by('title'))},"
            f" books average rating: {books_avg_rating:.1f}")


def get_authors_by_books_count() ->str:
    top_authors = (Author.objects
                   .annotate(num_main_books=Count('book', distinct=True))
                   .annotate(num_co_books=Count('books', distinct=True))
                   .annotate(sum_books=F('num_main_books') + F('num_co_books'))
                   .filter(sum_books__gt=0)
                   .order_by('-sum_books', 'name')
                   )[:3]

    if not top_authors.exists():
        return "No results."

    return '\n'.join(f"{a.name} authored {a.sum_books} books." for a in top_authors.all())

def get_bestseller() ->str:
    top_bestseller = (Book.objects
                      .prefetch_related('co_authors')
                      .select_related('main_author')
                      .filter(is_bestseller=True)
                      .annotate(num_co_authors=Count('co_authors', distinct=True))
                      .annotate(num_authors=F('num_co_authors') + 1)
                      .annotate(composite_index=F('rating') + F('num_authors'))
                      .order_by('-composite_index', '-rating', '-num_authors', 'title' )
                      .first()
                      )
    if top_bestseller is None:
        return 'No results.'


    if top_bestseller.num_co_authors == 0:
        result = 'N/A'
    else:
        result = '/'.join(a.name for a in top_bestseller.co_authors.all().order_by('name'))

    return (f"Top bestseller: {top_bestseller.title},"
            f" index: {top_bestseller.composite_index:.1f}."
            f" Main author: {top_bestseller.main_author.name}."
            f" Co-authors: {result}.")

print(get_bestseller())

def increase_price() ->str:
    YEAR=2025
    num_of_updated_books = (Book.objects
                       .select_related('publisher')
                       .filter(publication_date__year=YEAR)
                       .annotate(sum_rating=F('rating') + F('publisher__rating'))
                       .filter(sum_rating__gte=8.0)
                       .update(price=Case(
                            When(price__gt=50.0, then=ExpressionWrapper(F('price') * 1.10,
                                    output_field=DecimalField(max_digits=6, decimal_places=2))),
                            default= ExpressionWrapper(F('price') * 1.20,
                                    output_field=DecimalField(max_digits=6, decimal_places=2))
                                          )
                                )
                            )

    if num_of_updated_books == 0:
        return "No changes in price."

    return f"Prices increased for {num_of_updated_books} book/s."

