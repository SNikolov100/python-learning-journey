def boarding_passengers(capacity, *args):
    total_number_of_passengers = 0
    accommodate_passenger_benefit_programs = {}
    result = []
    max_passengers = 0
    start_capacity = capacity
    accommodated = True
    for passengers, program_name in args:
        max_passengers += passengers
        if passengers <= capacity:
            if program_name not in accommodate_passenger_benefit_programs:
                accommodate_passenger_benefit_programs[program_name] = 0
            accommodate_passenger_benefit_programs[program_name] += passengers
            capacity -= passengers
            total_number_of_passengers += passengers
        else:
            accommodated = False
        if capacity == 0:
            continue
    sorted_accommodate_passenger = sorted(accommodate_passenger_benefit_programs.items(), key=lambda x: (-x[1], x[0]))
    result.append("Boarding details by benefit plan:")
    for plan, passengers in sorted_accommodate_passenger:
        result.append(f"## {plan}: {passengers} guests")

    if accommodated :
        result.append("All passengers are successfully boarded!")
    elif capacity <= 0 and max_passengers > start_capacity:
        result.append("Boarding unsuccessful. Cruise ship at full capacity.")
    elif capacity > 0 and max_passengers > start_capacity:
        result.append(f"Partial boarding completed. Available capacity: {start_capacity - total_number_of_passengers}.")
    return "\n".join(result)











print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))
print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))
