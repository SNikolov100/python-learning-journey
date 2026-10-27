is_finish = False

total_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while True:
    counter_student = 0
    counter_standard = 0
    counter_kid = 0
    tickets_for_one_movie = 0
    name_movie = input()

    if name_movie == "Finish":
        is_finish = True
        break

    free_space_hall = int(input())

    for _ in range(free_space_hall):
        type_ticket = input()
        if type_ticket == "End":
            break
        elif type_ticket == "student":
            counter_student += 1
        elif type_ticket == "standard":
            counter_standard += 1
        elif type_ticket == "kid":
            counter_kid += 1
    tickets_for_one_movie += counter_student + counter_standard + counter_kid
    percent_full_hall = (tickets_for_one_movie * 100) / free_space_hall
    print(f"{name_movie} - {percent_full_hall:.2f}% full.")
    student_tickets += counter_student
    standard_tickets += counter_standard
    kid_tickets += counter_kid

total_tickets = (student_tickets + standard_tickets + kid_tickets)
percent_student_ticket = (student_tickets * 100) / total_tickets
percent_standard_ticket = (standard_tickets * 100) / total_tickets
percent_kid_ticket = (kid_tickets * 100) / total_tickets

if is_finish:
    print(f"Total tickets: {total_tickets}")
    print(f"{percent_student_ticket:.2f}% student tickets.")
    print(f"{percent_standard_ticket:.2f}% standard tickets.")
    print(f"{percent_kid_ticket:.2f}% kids tickets.")
