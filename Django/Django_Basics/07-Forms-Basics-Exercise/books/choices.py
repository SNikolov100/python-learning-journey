from django.db import models

class GenreChoices(models.TextChoices):
    FICTION = 'fiction', 'Fiction'
    NON_FICTION = 'non_fiction', 'Non Fiction'
    FANTASY = 'fantasy', 'Fantasy'
    SCIENCE = 'science', 'Science'

class LanguageChoices(models.TextChoices):
    BULGARIAN = 'bul', 'Bulgarian'
    ENGLISH = 'eng', 'English'
    FRENCH = 'fr', 'French'
    GERMAN = 'ger', 'German'
    OTHER = 'other', 'Other'