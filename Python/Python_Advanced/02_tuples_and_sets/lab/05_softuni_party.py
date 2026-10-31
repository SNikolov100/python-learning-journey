number_quest = int(input())
reservation_list = set()
vip= []
regular = []

for _ in range(number_quest):
    reservation_list.add(input())

while True:
    reservation_number = input()
    if reservation_number == "END":
        break
    if reservation_number in reservation_list:
        reservation_list.remove(reservation_number)

print(len(reservation_list))
reservation_list = sorted(reservation_list)
print(*reservation_list, sep="\n")