from django.db import models

class Review(models.Model):
    author = models.CharField(
        max_length=30
    )
    body = models.CharField(
        max_length=250
    )
    rating = models.DecimalField(
        max_digits=4,
        decimal_places=2
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE, related_name='reviews')

