from django.core.exceptions import ValidationError

def validate_rating_in_range(value:float):
    if not (0.0 <= value <= 10.00):
        ValidationError('The rating must be between 0.0 and 10.0')

def release_year_between_1990_2023(value:int):
    if not (1990 <= value <= 2023):
        ValidationError("The release year must be between 1990 and 2023")

