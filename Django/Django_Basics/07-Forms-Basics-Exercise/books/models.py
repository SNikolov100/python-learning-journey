from django.db import models
from django.template.defaultfilters import slugify

from core.base_models import TimestampMixin
from core.validators import FixedLengthValidator
from .choices import GenreChoices, LanguageChoices

class Book(TimestampMixin):
    title = models.CharField(
        max_length=50,
        unique=True
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    isbn = models.CharField(
        validators=[FixedLengthValidator(12)],
        unique=True
    )
    genre = models.CharField(
        choices=GenreChoices.choices
    )
    language = models.CharField(
        choices=LanguageChoices
    )
    pages = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    publishing_date = models.DateField()
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField(
        unique=True,
        blank=True,
        editable=False
    )
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.title}-{self.id}")
        super().save(*args, **kwargs)


