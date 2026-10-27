number_bad_grade = int(input())

last_task = ""
count_bad_grade = 0
count_grades = 0
max_score = 0
is_enough = False

while count_bad_grade < number_bad_grade:
    name_task = input()
    if name_task == "Enough":
        is_enough = True
        break
    grade = int(input())
    if grade <= 4:
        count_bad_grade += 1

    count_grades += 1
    max_score += grade
    last_task = name_task

average_score = max_score / count_grades

if is_enough:
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {count_grades}")
    print(f"Last problem: {last_task}")
else:
    print(f"You need a break, {count_bad_grade} poor grades.")


