count_fitness_man = int(input())
count_back = 0
count_chest = 0
count_legs = 0
count_abs = 0
count_protein_shake = 0
count_protein_bar = 0


for _ in range (count_fitness_man):
    action_activities = input()

    if action_activities == "Back":
        count_back += 1

    elif action_activities == "Chest":
        count_chest += 1

    elif action_activities == "Legs":
        count_legs += 1

    elif action_activities == "Abs":
        count_abs += 1

    elif action_activities == "Protein shake":
        count_protein_shake += 1

    elif action_activities == "Protein bar":
        count_protein_bar += 1

percent_train_people = ((count_back + count_chest + count_legs + count_abs) / count_fitness_man) * 100
percent_protein_people = ((count_protein_shake + count_protein_bar) / count_fitness_man) * 100

print(f"{count_back} - back")
print(f"{count_chest} - chest")
print(f"{count_legs} - legs")
print(f"{count_abs} - abs")
print(f"{count_protein_shake} - protein shake")
print(f"{count_protein_bar} - protein bar")
print(f"{percent_train_people:.2f}% - work out")
print(f"{percent_protein_people:.2f}% - protein")

