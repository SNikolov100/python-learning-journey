def students_credits(*args):
    result = []
    diyan_course = {}
    need_credits = 240
    total_credits = 0
    for data in args:
        course_name, course_credits, max_test_points, diyan_points = data.split("-")
        take_credits = float(course_credits) * (float(diyan_points) / float(max_test_points))
        diyan_course[course_name] = take_credits
        total_credits += take_credits
    sorted_courses = sorted(diyan_course.items(), key=lambda x: -x[1])

    if total_credits >= need_credits:
        result.append(f"Diyan gets a diploma with {total_credits:.1f} credits.")
    else:
        result.append(f"Diyan needs {(need_credits - total_credits):.1f} credits more for a diploma.")
    for course_name, diyan_credit in sorted_courses:
        result.append(f"{course_name} - {diyan_credit:.1f}")

    return '\n'.join(result)

print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)
print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
