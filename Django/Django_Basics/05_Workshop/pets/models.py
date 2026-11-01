from django.db import models
from django.template.defaultfilters import slugify


class Pet(models.Model):
    name = models.CharField(
        max_length=30,
    )
    personal_pet_photo = models.URLField()
    date_of_birth = models.DateField(
        blank=True  #optional
    )
    slug = models.CharField(
        unique=True,
        blank=True,
        editable=False,
    )
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.slug = slugify(f"{self.name}-{self.id}")
        super().save(*args, **kwargs)
