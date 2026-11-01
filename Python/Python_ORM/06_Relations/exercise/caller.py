import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

from main_app.models import Author, Book, Artist, Song, Product, Review, Driver, DrivingLicense, Owner, Registration, \
    Car
from django.db.models import QuerySet
from datetime import date, timedelta, datetime


# Create queries within functions
def show_all_authors_with_their_books() -> str:
    all_authors = Author.objects.all()
    authors_list = []

    for author in all_authors:
        books = author.book_set.all()
        if not books:
            continue
        titles = ', '.join(b.title for b in books)
        authors_list.append(f"{author.name} has written - {titles}!)")

    return '\n'.join(authors_list)

def delete_all_authors_without_books() ->None:
    Author.objects.filter(book__isnull=True).delete()


def add_song_to_artist(artist_name: str, song_title: str) ->None:
    artist = Artist.objects.get(name=artist_name)
    title = Song.objects.get(title= song_title)
    artist.songs.add(title)


def get_songs_by_artist(artist_name: str) ->QuerySet[Song]:
    songs = Artist.objects.get(name= artist_name).songs.order_by('-id')
    return songs


def remove_song_from_artist(artist_name: str, song_title: str) ->None:
    artist = Artist.objects.get(name= artist_name)
    song = Song.objects.get(title=song_title)
    artist.songs.remove(song)


def calculate_average_rating_for_product_by_name(product_name: str) ->float:
    product = Product.objects.get(name= product_name)
    reviews = product.reviews.all()
    avg_rating = sum(r.rating for r in reviews) / reviews.count()
    return avg_rating

def get_reviews_with_high_ratings(threshold: int) ->QuerySet[Review]:
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews() -> QuerySet[Product]:
    return Product.objects.filter(reviews__isnull=True).order_by('-name')

def delete_products_without_reviews() ->None:
    Product.objects.filter(reviews__isnull=True).delete()

def calculate_licenses_expiration_dates() ->str:
    all_licenses = DrivingLicense.objects.all().order_by('-license_number')
    return '\n'.join(f"License with number: {l.license_number} expires on {l.issue_date + timedelta(days=365)}!"
                     for l in all_licenses)

def get_drivers_with_expired_licenses(due_date: date) ->QuerySet[Driver]:
    due_date -= timedelta(365)
    all_drivers = Driver.objects.filter(license__issue_date__lt=due_date)
    return all_drivers

def register_car_by_owner(owner: Owner) ->str:
    registration= Registration.objects.filter(car__isnull=True).first()
    car = Car.objects.filter(registration__isnull=True).first()
    car.owner=owner
    car.registration =registration
    car.save()
    registration.registration_date = datetime.today()
    registration.car = car
    registration.save()
    return f"Successfully registered {car.model} to {owner.name} with registration number {registration.registration_number}."


