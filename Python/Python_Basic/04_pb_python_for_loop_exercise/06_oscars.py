POINTS_REWORD = 1250.5

name_actor = input()
points_from_academic = float(input())
number_of_judge = int(input())
name_judge = ""
points_judge = 0
reword = False

for _ in range(1, number_of_judge + 1):
    name_judge = input()
    points_judge = float(input())
    points_from_academic += (len(name_judge) * points_judge) / 2
    if points_from_academic >= POINTS_REWORD:
        reword = True
        break

if reword:
    print(f"Congratulations, {name_actor} got a nominee for leading role with {points_from_academic:.1f}!")
else:
    print(f"Sorry, {name_actor} you need {(POINTS_REWORD - points_from_academic):.1f} more!")


