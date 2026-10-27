number_groups = int(input())
count_people_musala = 0
count_people_monblan = 0
count_people_kilimandgaro = 0
count_people_k2 = 0
count_people_everest = 0
sum_people = 0
count_people = 0

for _ in range(number_groups):
    count_people = int(input())
    sum_people += count_people
    if count_people <= 5:
        count_people_musala += count_people
    elif 6 <= count_people <= 12:
        count_people_monblan += count_people
    elif 13 <= count_people <= 25:
        count_people_kilimandgaro += count_people
    elif 26 <= count_people <= 40:
        count_people_k2 += count_people
    else:
        count_people_everest += count_people

percent_people_musala = (count_people_musala * 100) / sum_people
percent_people_monblan = (count_people_monblan * 100) / sum_people
percent_people_kilimandgaro = (count_people_kilimandgaro * 100) / sum_people
percent_people_k2 = (count_people_k2 * 100) / sum_people
percent_people_everest = (count_people_everest * 100) / sum_people

print(f"{percent_people_musala:.2f}%")
print(f"{percent_people_monblan:.2f}%")
print(f"{percent_people_kilimandgaro:.2f}%")
print(f"{percent_people_k2:.2f}%")
print(f"{percent_people_everest:.2f}%")

