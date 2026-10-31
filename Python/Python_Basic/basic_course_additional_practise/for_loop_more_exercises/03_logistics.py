VAN_3T = 200
TRACK_4_11T = 175
TRAIN_12T = 120

count_cargo = int(input())
price_cargo = 0
count_ton = 0
count_van = 0
count_track = 0
count_train = 0


for _ in range(count_cargo):
    weight = int(input())
    count_ton += weight
    if weight <= 3:
        price_cargo += VAN_3T * weight
        count_van += weight
    elif 4 <= weight <= 11:
        price_cargo += TRACK_4_11T * weight
        count_track += weight
    elif weight >= 12:
        price_cargo += TRAIN_12T * weight
        count_train += weight

sum_cargo = count_van + count_track + count_train
average_price = price_cargo / count_ton
percent_van = (count_van * 100) / sum_cargo
percent_track = (count_track * 100) / sum_cargo
percent_train = (count_train * 100) / sum_cargo

print(f"{average_price:.2f}")
print(f"{percent_van:.2f}%")
print(f"{percent_track:.2f}%")
print(f"{percent_train:.2f}%")


