DELAY_PER_15_METERS = 12.5          # second

word_record = float(input())        # second
distance = float(input())           # meters
time_to_1_meter = float(input())    # seconds

finish_time = time_to_1_meter * distance
finish_time += (distance // 15) * DELAY_PER_15_METERS

if finish_time < word_record:
    print(f"Yes, he succeeded! The new world record is {finish_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {abs(finish_time - word_record):.2f} seconds slower.")