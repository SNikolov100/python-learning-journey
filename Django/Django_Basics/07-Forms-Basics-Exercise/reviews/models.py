from django.db import models
from core.base_models import TimestampMixin
from .choices import ReviewTypeChoices
from books.models import Book

class Review(TimestampMixin):
    author = models.CharField(
        max_length=50,
    )
    body = models.TextField()
    rating = models.DecimalField(
        max_digits=4,
        decimal_places=2
    )
    is_verified = models.BooleanField(default=False)
    review_type = models.CharField(
        choices=ReviewTypeChoices.choices
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews')





