percent_student_tickets = 0
percent_standard_tickets = 0
percent_kid_tickets = 0
total_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while True:
    name_movies = input()
    free_spaces = 0
    percent_free_spaces = 0

    if name_movies == "Finish":
        break

    free_places = int(input())

    for _ in range(free_places):
        info_tickets = input()

        if info_tickets == "End":
            break
        elif info_tickets == "student":
            free_spaces += 1
            student_tickets += 1
        elif info_tickets == "standard":
            free_spaces += 1
            standard_tickets += 1
        elif info_tickets == "kid":
            free_spaces += 1
            kid_tickets += 1

    percent_free_spaces = (free_spaces * 100) / free_places
    print(f"{name_movies} - {percent_free_spaces:.2f}% full.")

total_tickets = student_tickets + standard_tickets + kid_tickets
percent_student_tickets = (student_tickets * 100) / total_tickets
percent_standard_tickets = (standard_tickets * 100) / total_tickets
percent_kid_tickets = (kid_tickets * 100) / total_tickets

print(f"Total tickets: {total_tickets}")
print(f"{percent_student_tickets:.2f}% student tickets.")
print(f"{percent_standard_tickets:.2f}% standard tickets.")
print(f"{percent_kid_tickets:.2f}% kids tickets.")




