from django.db.models import Manager
from main_app.querysets import AstronautQuerySet

class AstronautManager(Manager.from_queryset(AstronautQuerySet)):
    def get_astronauts_by_missions_count(self):
        return self.by_missions_count()
