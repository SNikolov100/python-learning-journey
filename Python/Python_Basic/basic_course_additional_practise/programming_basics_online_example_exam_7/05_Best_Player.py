from sys import maxsize
goals_max = - maxsize
name_goal_player = ""
is_hat_trick = False

while True:
    name_player = input()
    if name_player == "END":
        break

    goals = int(input())

    if goals_max < goals:
        goals_max = goals
        name_goal_player = name_player

    if goals >= 10:
        break

print(f"{name_goal_player} is the best player!")

if goals_max >= 3:
    print(f"He has scored {goals_max} goals and made a hat-trick !!!")
else:
    print(f"He has scored {goals_max} goals.")








