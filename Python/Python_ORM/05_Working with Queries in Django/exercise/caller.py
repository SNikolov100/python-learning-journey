import os
from email.policy import default
from itertools import count

import django
from django.db.models.fields import TextField

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ArtworkGallery, Laptop, ChessPlayer, Meal, Dungeon, Workout
from main_app.choices import LaptopType, OperationSystemType
from django.db.models import When, Case, F, Value, PositiveIntegerField




# Import your models
# Create and check models
# Run and print your queries
def show_highest_rated_art() ->str:
    # art_name, rating = ArtworkGallery.objects.order_by('-rating', 'id').values('art_name','rating').first()
    # return f"{art_name} is the highest-rated art with a {rating} rating!"

    qs = ArtworkGallery.objects.order_by('-rating', 'id').first()
    return f"{qs.art_name} is the highest-rated art with a {qs.rating} rating!"

def bulk_create_arts(first_art: ArtworkGallery, second_art: ArtworkGallery):
    ArtworkGallery.objects.bulk_create([first_art,second_art])

def delete_negative_rated_arts():
    ArtworkGallery.objects.filter(rating__lt=0).delete()

def show_the_most_expensive_laptop() ->str:
    qs = Laptop.objects.order_by('-price', '-id').first()
    return f"{qs.brand} is the most expensive laptop available for {qs.price}$!"

def bulk_create_laptops(args: list[Laptop]) -> None:
    Laptop.objects.bulk_create(args)

def update_to_512_GB_storage() ->None:
    # Laptop.objects.filter(brand__in=[LaptopType.ASUS, LaptopType.LENOVO]).update(storage=512)

    Laptop.objects.update(storage=
        Case(When(brand__in= [LaptopType.ASUS, LaptopType.LENOVO],then=Value(512)),
             default=F('storage'),
             output_field=PositiveIntegerField()
             )
    )

def update_to_16_GB_memory() ->None:
    Laptop.objects.update(memory=
        Case(When(brand_in= [LaptopType.APPLE, LaptopType.DELL,LaptopType.ACER],then=Value(16)),
            default=F('memory'),
            output_field=PositiveIntegerField()
             )
    )

def update_operation_systems() ->None:
    Laptop.objects.update(operation_system=
        Case(
            When(brand = LaptopType.ASUS, then= Value(OperationSystemType.WINDOWS)),
            When(brand = LaptopType.APPLE, then= Value(OperationSystemType.MACOS)),
            When(brand__in = [LaptopType.DELL, LaptopType.ACER], then= Value(OperationSystemType.LINUX)),
            When(brand = LaptopType.LENOVO, then= Value(OperationSystemType.CHROME_OS)),
            default=F('operation_system')
        )
    )


def delete_inexpensive_laptops() ->None:
    Laptop.objects.filter(price__lt=1200).delete()


def bulk_create_chess_players(args: list[ChessPlayer]) -> None:
    ChessPlayer.objects.bulk_create(args)


def delete_chess_players() ->None:
    ChessPlayer.objects.filter(title='no title').delete()


def change_chess_game_won() ->None:
    ChessPlayer.objects.filter(title='GM').update(games_won=30)

def change_chess_game_lost() ->None:
    ChessPlayer.objects.filter(title='no title').update(games_lost=25)

def change_chess_game_drawn() ->None:
    ChessPlayer.objects.update(games_drawn= 10)

def grand_chess_title_GM() ->None:
    ChessPlayer.objects.filter(rating__gte=2400).update(title= 'GM')

def grand_chess_title_IM() ->None:
    ChessPlayer.objects.filter(rating__range=[2300, 2399]).update(title= 'IM')

def grand_chess_title_FM() ->None:
    ChessPlayer.objects.filter(rating__range=[2200, 2299]).update(title= 'FM')

def grand_chess_title_regular_player() ->None:
    ChessPlayer.objects.filter(rating__range=[0,2199]).update(title='regular player')

def set_new_chefs() ->None:
    Meal.objects.update(chef=
        Case(
            When(meal_type='Breakfast', then=Value('Gordon Ramsay')),
            When(meal_type='Lunch', then=Value('Julia Child')),
            When(meal_type='Dinner', then=Value('Jamie Oliver')),
            When(meal_type='Snack', then=Value('Thomas Keller')),
            default=F('chef')
        )
    )

def set_new_preparation_times() ->None:
    Meal.objects.update(preparation_time=
        Case(
            When(meal_type='Breakfast', then=Value('10 minutes')),
            When(meal_type='Lunch', then=Value('12 minutes')),
            When(meal_type='Dinner', then=Value('15 minutes')),
            When(meal_type='Snack', then=Value('5 minutes')),
            default=F('preparation_time')
        )
    )

def update_low_calorie_meals() ->None:
    Meal.objects.update(calories=
        Case(
            When(meal_type__in=['Breakfast', 'Dinner'], then=Value(400)),
            default=F('calories')
        )
    )

def update_high_calorie_meals() ->None:
    Meal.objects.update(calories=
        Case(
            When(meal_type__in=['Lunch', 'Snack'], then=Value(700)),
            default=F('calories')
        )
    )

def delete_lunch_and_snack_meals() ->None:
    Meal.objects.filter(meal_type__in=['Lunch', 'Snack']).delete()


def show_hard_dungeons() ->str:
    hard_dungeons = Dungeon.objects.filter(difficulty='Hard').order_by('-location')
    return '\n'.join(f"{hd.name} is guarded by {hd.boss_name} who has {hd.boss_health} health points!"
                     for hd in hard_dungeons)

def bulk_create_dungeons(args: list[Dungeon]) ->None:
    Dungeon.objects.bulk_create(args)

def update_dungeon_names() ->None:
    Dungeon.objects.update(name=
        Case(
            When(difficulty='Easy', then=Value('The Erased Thombs')),
            When(difficulty='Medium', then=Value('The Coral Labyrinth')),
            When(difficulty='Hard', then=Value('The Lost Haunt')),
            default=F('name')
        )
    )

def update_dungeon_bosses_health() ->None:
    Dungeon.objects.exclude(difficulty='Easy').update(boss_health=500)

def update_dungeon_recommended_levels() ->None:
    Dungeon.objects.update(recommended_level=
        Case(
            When(difficulty='Easy', then=Value(25)),
            When(difficulty='Medium', then=Value(50)),
            When(difficulty='Hard', then=Value(75)),
            default=F('recommended_level')
        )
    )

def update_dungeon_rewards() ->None:
    Dungeon.objects.filter(boss_health=500).update(reward='1000 Gold')
    Dungeon.objects.filter(location__startswith="E").update(reward='New dungeon unlocked')
    Dungeon.objects.filter(location__endswith='s').update(reward='Dragonheart Amulet')

    # Dungeon.objects.update(reward=
    #     Case(
    #         When(boss_health=500, then=Value('1000 Gold')),
    #         When(location__startswith='E', then=Value('New dungeon unlocked')),
    #         When(location__endswith='s', then=Value('Dragonheart Amulet')),
    #         default=F('reward'),
    #         output_field=TextField()
    #     )
    # )

def set_new_locations() ->None:
    Dungeon.objects.update(location=
        Case(
            When(recommended_level=25, then=Value('Enchanted Maze')),
            When(recommended_level=50, then=Value('Grimstone Mines')),
            When(recommended_level=75, then=Value('Shadowed Abyss')),
            default=F('location')
        )
    )


def show_workouts() ->str:
    workout_qs = Workout.objects.filter(workout_type__in=['Calisthenics','CrossFit']).order_by('id')
    return '\n'.join(f"{w.name} from {w.workout_type} type has {w.difficulty} difficulty!" for w in workout_qs)

def get_high_difficulty_cardio_workouts():
    return Workout.objects.filter(workout_type='Cardio', difficulty='High').order_by('instructor')

def set_new_instructors() ->None:
    Workout.objects.update(instructor=
        Case(
            When(workout_type='Cardio', then=Value('John Smith')),
            When(workout_type='Strength', then=Value('Michael Williams')),
            When(workout_type='Yoga', then=Value('Emily Johnson')),
            When(workout_type='CrossFit', then=Value('Sarah Davis')),
            When(workout_type='Calisthenics', then=Value('Chris Heria')),
            default=F('instructor')
        )
    )

def set_new_duration_times() ->None:
    Workout.objects.update(duration=
        Case(
            When(instructor='John Smith', then=Value('15 minutes')),
            When(instructor='Sarah Davis', then=Value('30 minutes')),
            When(instructor='Chris Heria', then=Value('45 minutes')),
            When(instructor='Michael Williams', then=Value('1 hour')),
            When(instructor='Emily Johnson', then=Value('1 hour and 30 minutes')),
            default=F('duration')
        )
    )

def delete_workouts() ->None:
    Workout.objects.exclude(workout_type__in=['Strength', 'Calisthenics']).delete()
