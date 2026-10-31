from collections import deque

mountain_peaks = (
    ("Vihren", 80),
    ("Kutelo", 90),
    ("Banski Suhodol", 100),
    ("Polezhan", 60),
    ("Kamenitza", 70),
)

daily_portions = [int(p) for p in input().split(", ")]
daily_stamina = deque(int(st) for st in input().split(", "))
conquered_peaks = []

for peak, level in mountain_peaks:
    while daily_portions and daily_stamina:
        first_portion = daily_portions.pop()
        last_stamina = daily_stamina.popleft()
        sum_endurance = first_portion + last_stamina
        if sum_endurance >= level:
            conquered_peaks.append(peak)
            break
    else:
        break

if len(conquered_peaks) == len(mountain_peaks):
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    print('\n'.join(cp for cp in conquered_peaks))


