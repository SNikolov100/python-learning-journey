from django.core.exceptions import ValidationError
from django.db import models
from django.template.defaultfilters import length


def validator_content_only_letters_spaces(value: str) ->None:
   for v in value:
       if not (v.isalpha() or v.isspace()):
           raise ValidationError('Name can only contain letters and spaces')

