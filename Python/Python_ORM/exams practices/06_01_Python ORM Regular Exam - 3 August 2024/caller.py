import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()
from datetime import date
from main_app.models import Astronaut, Spacecraft, Mission
from django.db.models import Q, Count, Sum, F, Avg


# Import your models here

def populate_db():
    # Astronauts
    a1 = Astronaut.objects.create(
        name="Neil Armstrong",
        phone_number="1111111111",
        date_of_birth=date(1930, 8, 5),
        spacewalks=2
    )

    a2 = Astronaut.objects.create(
        name="Buzz Aldrin",
        phone_number="2222222222",
        date_of_birth=date(1930, 1, 20),
        spacewalks=3
    )

    a3 = Astronaut.objects.create(
        name="Sally Ride",
        phone_number="3333333333",
        date_of_birth=date(1951, 5, 26),
        spacewalks=1
    )

    a4 = Astronaut.objects.create(
        name="Yuri Gagarin",
        phone_number="4444444444",
        date_of_birth=date(1934, 3, 9),
        spacewalks=0
    )

    a5 = Astronaut.objects.create(
        name="Valentina Tereshkova",
        phone_number="5555555555",
        date_of_birth=date(1937, 3, 6),
        spacewalks=0
    )

    # Spacecrafts
    s1 = Spacecraft.objects.create(
        name="Apollo 11",
        manufacturer="NASA",
        capacity=3,
        weight=28801.0,
        launch_date=date(1969, 7, 16)
    )

    s2 = Spacecraft.objects.create(
        name="Soyuz MS",
        manufacturer="Roscosmos",
        capacity=3,
        weight=7220.0,
        launch_date=date(2020, 4, 9)
    )

    s3 = Spacecraft.objects.create(
        name="Crew Dragon",
        manufacturer="SpaceX",
        capacity=4,
        weight=12500.0,
        launch_date=date(2021, 11, 11)
    )

    s4 = Spacecraft.objects.create(
        name="Orion",
        manufacturer="NASA",
        capacity=6,
        weight=26000.0,
        launch_date=date(2022, 11, 16)
    )

    s5 = Spacecraft.objects.create(
        name="Starliner",
        manufacturer="Boeing",
        capacity=5,
        weight=13000.0,
        launch_date=date(2024, 6, 5)
    )

    # Missions
    m1 = Mission.objects.create(
        name="Moon Landing",
        description="First human moon landing",
        status=Mission.StatusType.COMPLETED,
        launch_date=date(1969, 7, 16),
        spacecraft=s1,
        commander=a1
    )

    m2 = Mission.objects.create(
        name="ISS Supply",
        description="Resupply mission",
        status=Mission.StatusType.ONGOING,
        launch_date=date(2025, 5, 10),
        spacecraft=s2,
        commander=a2
    )

    m3 = Mission.objects.create(
        name="Mars Research",
        description="Research mission",
        status=Mission.StatusType.PLANNED,
        launch_date=date(2027, 8, 1),
        spacecraft=s3,
        commander=a3
    )

    m4 = Mission.objects.create(
        name="Lunar Base",
        description="Building lunar base",
        status=Mission.StatusType.PLANNED,
        launch_date=date(2028, 3, 15),
        spacecraft=s4,
        commander=a4
    )

    m5 = Mission.objects.create(
        name="Deep Space",
        description="Long distance exploration",
        status=Mission.StatusType.PLANNED,
        launch_date=date(2029, 10, 10),
        spacecraft=s5,
        commander=a5
    )

    # Many-to-Many
    m1.astronauts.add(a1, a2)
    m2.astronauts.add(a2, a3)
    m3.astronauts.add(a3, a4)
    m4.astronauts.add(a4, a5)
    m5.astronauts.add(a1, a3, a5)


def get_astronauts(search_string=None) ->str:
    if search_string is None:
        return ""
    find_astronauts = (Astronaut.objects
                      .filter(Q(name__icontains=search_string)
                              |
                              Q(phone_number__icontains=search_string))
                      .order_by('-name')
                      )
    if not find_astronauts.exists():
        return ""

    return '\n'.join(f"Astronaut: {a.name}, phone number: {a.phone_number}, status: {'Active' if a.is_active else 'Inactive'}" for a in find_astronauts.all())

def get_top_astronaut() ->str:
    top_astronaut = Astronaut.objects.get_astronauts_by_missions_count().filter(number_of_missions__gt=0).first()
    if top_astronaut is None:
        return "No data."

    return f"Top Astronaut: {top_astronaut.name} with {top_astronaut.number_of_missions} missions."

def get_top_commander():
    top_commander = (Astronaut.objects
                     .annotate(num_of_missions=Count('missions'))
                     .filter(num_of_missions__gt=0)
                     .order_by('-num_of_missions', 'phone_number')
                     .first()
                     )
    if top_commander is None:
        return "No data."

    return f"Top Commander: {top_commander.name} with {top_commander.num_of_missions} commanded missions."

def get_last_completed_mission() ->str:
    last_mission = (Mission.objects
                    .prefetch_related('astronauts')
                    .select_related('commander', 'spacecraft')
                    .annotate(total_spacewalks=Sum('astronauts__spacewalks'))
                    .filter(status=Mission.StatusType.COMPLETED)
                    .order_by('launch_date')
                    .last()
                    )
    if last_mission is None:
        return "No data."

    return (f"The last completed mission is: {last_mission.name}."
            f" Commander: {'TBA' if last_mission.commander.name is None else last_mission.commander.name}."
            f" Astronauts: {', '.join(a.name for a in last_mission.astronauts.all().order_by('name'))}."
            f" Spacecraft: {last_mission.spacecraft.name}."
            f" Total spacewalks: {last_mission.total_spacewalks}.")


def decrease_spacecrafts_weight() ->str:
    num_of_spacecrafts_affected = (Spacecraft.objects
                          .filter(mission__status=Mission.StatusType.PLANNED,
                                  weight__gte=200)
                          .values_list('id', flat=True)
                          .update(weight=F('weight') - 200)
                          )

    if num_of_spacecrafts_affected == 0:
        return "No changes in weight."

    avg_weight = Spacecraft.objects.aggregate(Avg('weight'))

    return (f"The weight of {num_of_spacecrafts_affected} spacecrafts has been decreased."
            f" The new average weight of all spacecrafts is {avg_weight['weight__avg']:.1f}kg")

