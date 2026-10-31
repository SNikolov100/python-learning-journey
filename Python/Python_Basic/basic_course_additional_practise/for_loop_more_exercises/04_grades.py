number_students = int(input())
grade_up_5 = 0
grade_between_45 = 0
grade_between_34 = 0
grade_under_3 = 0
sum_grade = 0


for _ in range(number_students):
    grade = float(input())
    sum_grade += grade
    if 2 <= grade <= 2.99:
        grade_under_3 += 1
    elif 3 <= grade <= 3.99:
        grade_between_34 += 1
    elif 4 <= grade <= 4.99:
        grade_between_45 += 1
    elif grade >= 5:
        grade_up_5 += 1

percent_up_5 = (grade_up_5 * 100) / number_students
percent_bw_45 = (grade_between_45 * 100) / number_students
percent_bw_34 = (grade_between_34 * 100) / number_students
percent_under_3 = (grade_under_3 * 100) / number_students
average_grade = sum_grade / number_students
print (f"Top students: {percent_up_5:.2f}%")
print (f"Between 4.00 and 4.99: {percent_bw_45:.2f}%")
print (f"Between 3.00 and 3.99: {percent_bw_34:.2f}%")
print (f"Fail: {percent_under_3:.2f}%")
print (f"Average: {average_grade:.2f}")
