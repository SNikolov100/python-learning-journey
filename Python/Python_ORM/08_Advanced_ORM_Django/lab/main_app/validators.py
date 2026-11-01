from django.core.exceptions import ValidationError

def validate_menu_categories(value):
    categories_list = ["Appetizers", "Main Course", "Desserts"]
    for category in categories_list:
        if category not in value:
            raise ValidationError('The menu must include each of the categories "Appetizers", "Main Course", "Desserts".')
