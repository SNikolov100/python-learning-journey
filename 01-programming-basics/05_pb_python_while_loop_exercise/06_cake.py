cake_size = int(input()) * int(input())

piece_cake = 0
is_Stop = True

while cake_size > 0:
    cake_data = input()

    if cake_data == "STOP":
        is_Stop = False
        break

    piece_cake = int(cake_data)
    cake_size -= piece_cake

if cake_size < 0:
    print(f"No more cake left! You need {abs(cake_size)} pieces more.")
else:
    print(f"{cake_size} pieces are left.")



