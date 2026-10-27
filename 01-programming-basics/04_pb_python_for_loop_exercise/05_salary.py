PENALTY_FACEBOOK = 150
PENALTY_INSTAGRAM = 100
PENALTY_REDDIT = 50

open_tabs = int(input())
salary = float(input())

end_salary = False
name_tab = ""
penalty = 0

for _ in range(1, open_tabs + 1):
    penalty = 0
    name_tab = input()
    if name_tab == "Facebook":
        penalty = PENALTY_FACEBOOK
    elif name_tab == "Instagram":
        penalty = PENALTY_INSTAGRAM
    elif name_tab == "Reddit":
        penalty = PENALTY_REDDIT
    salary -= penalty
    if salary <= 0:
        end_salary = True
        break

if end_salary:
    print("You have lost your salary.")
else:
    print(f"{salary:.0f}")

