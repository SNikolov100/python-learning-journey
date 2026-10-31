number_students = int(input())

data_students = {}

for _ in range(number_students):
    name_student, grade = input().split()
    if name_student not in data_students:
        data_students[name_student]= []
    data_students[name_student].append(float(grade))

for name_student, grade in data_students.items():
    average_grade = sum(grade) / len(grade)
    print(f"{name_student} -> {' '.join(f'{x:.2f}' for x in grade)} (avg: {average_grade:.2f})")

