average_grade_all = 0
name_presentation = ""
sum_grade_all = 0
project = 0

judge = int(input())

while True:
    average_grade_per_student = 0
    name_presentation = input()
    sum_grade = 0
    if name_presentation == "Finish":
        break
    for _ in range(judge):
        grade = float(input())
        sum_grade += grade

    average_grade_per_student = sum_grade / judge
    sum_grade_all += average_grade_per_student
    project += 1
    print(f"{name_presentation} - {average_grade_per_student:.2f}.")

average_grade_all = sum_grade_all / project

print(f"Student's final assessment is {average_grade_all:.2f}.")