from django.db import models

class ReviewTypeChoices(models.TextChoices):
    TEXT = 'text', 'Text'
    VIDEO = 'video', 'Video'
    AUDIO = 'audio', 'Audio'