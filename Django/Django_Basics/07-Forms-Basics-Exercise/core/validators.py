from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class FixedLengthValidator:
    def __init__(self, value):
        self.value = value
    def __call__(self, input_text):
        if len(input_text) != self.value:
            raise ValidationError(f"The text must be exactly {self.value} characters")
