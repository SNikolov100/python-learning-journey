from django.core.validators import MinLengthValidator
from django.db import models

from pets.models import Pet
from pets.validators import FileSizeValidator


class Photo(models.Model):
    photo = models.ImageField(
        upload_to='photos/',
        validators=[
            FileSizeValidator(5),
        ]
    )
    description = models.CharField(
        max_length=300,
        validators=[
            MinLengthValidator(10, message='Description must be at least 10 characters long.')
        ],
        blank=True,
        null=True,
    )
    location = models.CharField(
        max_length=30,
    )
    tagged_pets = models.ManyToManyField(
        to='pets.Pet',
    )
    date_of_publication = models.DateField(
        auto_now=True
    )
