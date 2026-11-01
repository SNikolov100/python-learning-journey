from django.db import models
from django.utils.text import slugify

from books.validators import FixedLengthValidator


class Book(models.Model):
    class GenreChoices(models.IntegerChoices):
        FICTION = 1, "Fiction"
        NON_FICTION = 2, "Non-Fiction"
        FANTASY = 3, "Fantasy"
        SCIENCE = 4, "Science"

    title = models.CharField(
        max_length=20,
        unique=True
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    isbn = models.CharField(
        max_length=12,
        validators=[
            FixedLengthValidator(12)
        ],
        unique=True
    )
    genre = models.IntegerField(
        choices=GenreChoices.choices,
    )
    published_date = models.DateField()
    description = models.TextField(
        blank=True,
    )
    image_url = models.URLField()
    slug = models.SlugField(
        unique=True,
        blank=True,
        editable=False
    )
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.title}-{self.pk}")
        super().save(*args, **kwargs)

    updated_at = models.DateTimeField(
        auto_now=True
    )




