min_on_control = int(input()) * 60
sec_on_control = int(input())
range_trace = float(input())
sec_for_100_meters = int(input())
counter_seconds = 0
result = 0
time_control = min_on_control + sec_on_control

late = (range_trace / 120) * 2.5
full_time = (range_trace / 100) * sec_for_100_meters - late

result = abs(time_control - full_time)
if full_time <= time_control:
    print(f"Marin Bangiev won an Olympic quota!\n"
          f"His time is {full_time:.3f}.")
else:
    print(f"No, Marin failed! He was {result:.3f} second slower.")




