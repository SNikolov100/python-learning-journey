from django.core.exceptions import ValidationError


def phone_number_contain_only_digits(value):
    if not value.isdigit():
        raise ValidationError
    return value

