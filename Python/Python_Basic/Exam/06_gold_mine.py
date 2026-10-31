number_location = int(input())


for location in range(1,number_location + 1):
    total_gold_per_location = 0
    expect_cold_per_day = float(input())
    number_days = int(input())
    for day in range(1, number_days + 1):
        get_gold_per_day = float(input())
        total_gold_per_location += get_gold_per_day
    average_gold_per_location = total_gold_per_location / number_days

    diff = average_gold_per_location - expect_cold_per_day
    if diff >= 0:
        print(f"Good job! Average gold per day: {average_gold_per_location:.2f}.")
    else:
        print(f"You need {abs(diff):.2f} gold.")

