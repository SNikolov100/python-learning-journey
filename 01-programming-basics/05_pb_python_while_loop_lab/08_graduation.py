name_student = input()
second_chance = True
class_student = 0
sum_grade = 0
grade = 0

while True:
    grade = float(input())
    if grade < 4:
        if second_chance:
            second_chance = False
            continue
        else:
            print(f"{name_student} has been excluded at {class_student + 1} grade")
            break
    class_student += 1
    sum_grade += grade
    if class_student == 12:
        average_grade = sum_grade / class_student
        print(f"{name_student} graduated. Average grade: {average_grade:.2f}")
        break


