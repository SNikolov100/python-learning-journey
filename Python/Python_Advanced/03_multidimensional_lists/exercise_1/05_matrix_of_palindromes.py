rows, cols = [int(x) for x in input().split()]
start_pos = ord("a")

for row in range(rows):
    for col in range(cols):
        print(f"{chr(row + start_pos)}{chr(row + col + start_pos)}{chr(row + start_pos)}", end=" ")
    print()
