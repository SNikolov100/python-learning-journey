def gather_credits(number_credits, *args):
    course_list = []
    result = []
    gathered_credits = 0
    for course_name, course_credit in args:
        if gathered_credits < number_credits:
            if course_name not in course_list:
                gathered_credits += course_credit
                course_list.append(course_name)
        else:
            break
    sorted_course_list = sorted(course_list, key=lambda x: x)
    if gathered_credits >= number_credits:
        result.append(f"Enrollment finished! Maximum credits: {gathered_credits}.")
        result.append(f"Courses: {', '.join(c for c in sorted_course_list) }")
    else:
        result.append(f"You need to enroll in more courses! You have to gather {number_credits - gathered_credits} credits more.")
    return '\n'.join(result)

print(gather_credits(
    80,
    ("Basics", 27),
))
print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
