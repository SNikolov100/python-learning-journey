name_actor = input()
points_for_oscar = float(input())
number_grade_person = int(input())
is_Receive = False

for _ in range(number_grade_person):

    name_grade = input()
    points_from_grade_person = float(input())
    length_name = len(name_grade)
    points_for_oscar += (length_name * points_from_grade_person) / 2
    if points_for_oscar > 1250.5:
        is_Receive = True
        break

if is_Receive:
    print(f"Congratulations, {name_actor} got a nominee for leading role with {points_for_oscar:.1f}!")
else:
    print(f"Sorry, {name_actor} you need {(1250.5 - points_for_oscar):.1f} more!")
