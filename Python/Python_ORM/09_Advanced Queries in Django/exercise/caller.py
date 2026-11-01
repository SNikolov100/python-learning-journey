import os


import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()
from datetime import date
# Import your models here
from main_app.models import RealEstateListing, VideoGame, Invoice, BillingInfo, Programmer, Technology, Project, Task, \
    Exercise
