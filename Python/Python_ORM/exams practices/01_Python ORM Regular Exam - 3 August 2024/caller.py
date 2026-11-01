import os

import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Astronaut, Mission, Spacecraft
from django.db.models import Q, Sum, Count, F
from django.db.models.aggregates import Avg


# Import your models here

# Create queries within functions
def get_astronauts(search_string=None) ->str:
    if search_string is None:
        return ""
    astronauts = Astronaut.objects.filter(
        Q(name__icontains=search_string) | Q(phone_number__icontains=search_string)
    ).order_by('name')
    if not astronauts.exists():
        return ""
    return '\n'.join(f"Astronaut: {a.name}, phone number: {a.phone_number}, status: {'Active' if a.is_active else 'Inactive'}" for a in astronauts)

def get_top_astronaut() ->str:
    top_astronaut = Astronaut.objects.annotate(
        sum_missions=Count('missions')
    ).filter(sum_missions__gt=0).order_by('-sum_missions', 'phone_number').first()
    if top_astronaut is None:
        return "No data."
    return f"Top Astronaut: {top_astronaut.name} with {top_astronaut.sum_missions} missions."

def get_top_commander() ->str:
    top_commander = Astronaut.objects.annotate(
        sum_commander= Count('commanded_missions')
    ).filter(sum_commander__gt=0).order_by('sum_commander', 'phone_number').first()
    if top_commander is None:
        return "No data."
    return f"Top Commander: {top_commander.name} with {top_commander.sum_commander} commanded missions."


def get_last_completed_mission() ->str:
    last_mission = (Mission.objects
                    .filter(status=Mission.StatusType.COMPLETED)
                    .select_related('spacecraft', 'commander')
                    .annotate(total_spacewalks=Sum('astronauts__spacewalks'))
                    .order_by('-launch_date')
                    .first()
    )
    if last_mission is None:
        return "No data."
    commander_name = last_mission.commander.name if last_mission.commander.name else "TBA"
    return (f"The last completed mission is: {last_mission.name}."
            f" Commander: {commander_name}."
            f" Astronauts: {', '.join(lm.name for lm in last_mission.astronauts.all().order_by('name'))}."
            f" Spacecraft: {last_mission.spacecraft.name}. Total spacewalks: {last_mission.total_spacewalks}.")

def get_most_used_spacecraft() ->str:
    max_spacecraft = (Spacecraft.objects
                      .prefetch_related('mission_set')
                      .annotate(
                            count_mission=Count('mission__id', distinct=True),
                            num_astronauts=Count('mission__astronauts__id', distinct=True)
                      )
                      .filter(count_mission__gt=0)
                      .order_by('-count_mission', 'name')
                      .first()
    )
    if max_spacecraft is None:
        return "No data."

    return (f"The most used spacecraft is: {max_spacecraft.name}"
            f", manufactured by {max_spacecraft.manufacturer}"
            f", used in {max_spacecraft.count_mission} missions"
            f", astronauts on missions: {max_spacecraft.num_astronauts}.")


def decrease_spacecrafts_weight() ->str:
    unique_spacecraft_ids = (Spacecraft.objects
                         .filter(mission__status=Mission.StatusType.PLANNED, weight__gte=200.0)
                         .values_list('id', flat=True)
                         .distinct()
                         )

    spacecraft_update = Spacecraft.objects.filter(id__in=unique_spacecraft_ids).update(weight=F('weight') - 200.0)

    if spacecraft_update == 0:
        return "No changes in weight."

    avg_weight = Spacecraft.objects.aggregate(avg_weight=Avg('weight'))['avg_weight']

    return (f"The weight of {spacecraft_update} spacecrafts has been decreased."
            f" The new average weight of all spacecrafts is {avg_weight:.1f}kg")











