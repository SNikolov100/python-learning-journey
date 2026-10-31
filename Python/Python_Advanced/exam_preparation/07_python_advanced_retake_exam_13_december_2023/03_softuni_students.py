def softuni_students(*args, **kwargs):
    username_courses_dict = {}
    invalid_course = []
    result = []
    for course_id, username in args:
        if course_id in kwargs:
            username_courses_dict[username] = kwargs[course_id]
        else:
            invalid_course.append(username)
    sorted_list = sorted(username_courses_dict.items(), key=lambda x: x[0])
    sorted_invalid_username = sorted(invalid_course)
    for username, course_name in sorted_list:
        result.append(f"*** A student with the username {username} has successfully finished the course {course_name}!")
    if sorted_invalid_username:
        result.append(f"!!! Invalid course students: {', '.join(name for name in sorted_invalid_username)}")
    return '\n'.join(result)



print(softuni_students(
    ('id_1', 'Kaloyan9905'),
    id_1='Python Web Framework',
))

print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))

print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))
