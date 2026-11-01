from django.core.exceptions import ValidationError
from django.template.defaultfilters import length
from django.utils.deconstruct import deconstructible


@deconstructible
class FixedLengthValidator:
    def __init__(self, value:int):
        self.value = value

    def __call__(self, input_text:str):
        if  len(input_text) != self.value:
            raise ValidationError(f"The text must consist {self.value} characters")


