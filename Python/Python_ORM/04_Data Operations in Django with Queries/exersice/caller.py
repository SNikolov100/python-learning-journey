import os


import django
from unicodedata import category

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

# Create queries within functions
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character
from django.db.models import Case, Value, When, QuerySet, F
from decimal import Decimal
from django.db.models.functions import Mod

def create_pet(name: str, species: str) -> str:
    Pet.objects.create(name=name, species=species)
    return f"{name} is a very cute {species}!"


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool) -> str:
    Artifact.objects.create(
        name= name,
        origin = origin,
        age = age,
        description = description,
        is_magical = is_magical
    )
    return f"The artifact {name} is {age} years old!"

def rename_artifact(artifact: Artifact, new_name : str):
     # for a in Artifact.objects.all():
     #     if a.is_magical and a.age > 250:
     #         a.name = new_name
     #         a.save()
    Artifact.objects.filter(
        is_magical=True,
        age__gt=250
    ).update(name = new_name)

def delete_all_artifacts():
    Artifact.objects.all().delete()


def show_all_locations() -> str:
    return '\n'.join(
        f"{name} has a population of {population}!"
        for name, population in Location.objects.values_list('name', 'population'))

def new_capital() ->None:
    l = Location.objects.first()
    # l.is_capital = True
    # l.save()
    if l:
        Location.objects.filter(pk=l.pk).update(is_capital=True)

def get_capitals() -> QuerySet:
    return Location.objects.filter(is_capital=True).values('name')

def delete_first_location():
    Location.objects.first().delete()

def apply_discount():
    # all_car = Car.objects.all()
    # for car in all_car:
    #     discount_present = Decimal(str(sum(int(ch) for ch in str(car.year)) /100))
    #     price_discount = discount_present * car.price
    #     car_price_discount = car.price - price_discount
    #     car.price_with_discount = car_price_discount
    #     car.save()
    list_cars = list(Car.objects.all())
    for car in list_cars:
        discount_persent = Decimal(str(sum(int(ch) for ch in str(car.year)) / 100))
        car.price_with_discount = car.price - (discount_persent * car.price)
    Car.objects.bulk_update(list_cars, ['price_with_discount'])

def get_recent_cars() -> QuerySet:
    return Car.objects.filter(year__gt=200).values('model')

def delete_last_car():
    Car.objects.last().delete()


def show_unfinished_tasks() ->str:
    return '\n'.join(
        f"Task - {title} needs to be done until {due_date}!"
        for title, due_date in
        Task.objects.filter(is_finished=False).values_list('title', 'due_date')
    )

def complete_odd_tasks():
    # all_tasks = Task.objects.all()
    # for task in all_tasks:
    #     if not task.id % 2 == 0:
    #         task.is_finished = True
    #         task.save()

    all_task_list = list(Task.objects.all())
    for task in all_task_list:
        if task.id % 2 != 0:
            task.is_finished = True
    Task.objects.bulk_update(all_task_list, ['is_finished'])

def encode_and_replace(text: str, task_title: str):
    new_text = ''
    new_text = new_text.join(chr(ord(ch)-3) for ch in text)
    Task.objects.filter(title=task_title).update(description=new_text)

def get_deluxe_rooms():
    # all_room_list = list(HotelRoom.objects.filter(room_type=HotelRoom.RoomType.DELUXE))
    # even_room = list()
    # for room in all_room_list:
    #     if room.id % 2 == 0:
    #         even_room.append(room)
    even_room_deluxe =(HotelRoom.objects
                       .filter(room_type=HotelRoom.RoomType.DELUXE)
                       .annotate(r=Mod(F('id'), 2))
                       .filter(r=0))
    return '\n'.join(
        f"Deluxe room with number {r.room_number} costs {r.price_per_night}$ per night!"
        for r in even_room_deluxe)

def increase_room_capacity():
    all_rooms = list(HotelRoom.objects.all().order_by('id'))
    for i in range(len(all_rooms)):
        if not all_rooms[i].is_reserved:
            continue
        if i == 0:
            all_rooms[i].capacity += all_rooms[i].id
        else:
            all_rooms[i].capacity += all_rooms[i-1].capacity
    HotelRoom.objects.bulk_update(all_rooms, ['capacity'])

def reserve_first_room():
    first_room = HotelRoom.objects.first()
    if first_room:
        HotelRoom.objects.filter(pk = first_room.pk).update(is_reserved=True)

def delete_last_room():
    HotelRoom.objects.filter(is_reserved=False).last().delete()

def update_characters():
    (Character.objects.filter(class_name=Character.ClassName.MAGE)
                        .update(level=F('level')+3, intelligence= F('intelligence')-7))
    (Character.objects.filter(class_name=Character.ClassName.WARRIOR)
                        .update(hit_points=F('hit_points') / 2, dexterity= F('dexterity')+4))
    (Character.objects.filter(class_name__in=[Character.ClassName.ASSASSIN, Character.ClassName.SCOUT])
                        .update(inventory= 'The inventory is empty'))

def fuse_characters(first_character: Character, second_character: Character):

    Character.objects.create(
        name= f"{first_character.name} {second_character.name}",
        class_name= 'Fusion',
        level= abs(int((first_character.level + second_character.level) // 2)),
        strength= abs(int((first_character.strength + second_character.strength) * 1.2)),
        dexterity= abs(int((first_character.dexterity + second_character.dexterity) * 1.4)),
        intelligence= abs(int((first_character.intelligence + second_character.intelligence) * 1.5)),
        hit_points= (first_character.hit_points + second_character.hit_points),
        inventory= 'Bow of the Elven Lords, Amulet of Eternal Wisdom'
            if first_character.class_name in [Character.ClassName.MAGE, Character.ClassName.SCOUT]
            else 'Dragon Scale Armor, Excalibur'
    )
    first_character.delete()
    second_character.delete()

def grand_dexterity():
    Character.objects.update(dexterity= 30)

def grand_intelligence():
    Character.objects.update(intelligence= 40)

def grand_strength():
    Character.objects.update(strength= 50)

def delete_characters():
    Character.objects.filter(inventory='The inventory is empty').delete()




