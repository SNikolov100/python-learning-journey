from django.core.exceptions import ValidationError
from django.db import models

def phone_number_only_digits(value):
    if not value.isdigit():
        raise ValidationError
    return value