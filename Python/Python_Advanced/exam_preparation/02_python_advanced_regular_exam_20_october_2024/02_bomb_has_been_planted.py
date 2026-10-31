maper ={
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

n, m = map(int, input().split(", "))
field_mat = []
enough_time = 16
counter_terrorist = ()
terrorist = set()
bomb = ()
on_bomb = False

for row in range(n):
    field_mat.append(list(input()))
    for col in range(m):
        if field_mat[row][col] == "C":
            counter_terrorist = (row, col )
        elif field_mat[row][col] == "T":
            terrorist.add((row, col))
        elif field_mat[row][col] == "B":
            bomb = (row, col)
start_r, start_c = counter_terrorist

while True:
    command = input()
    if command in maper:
        enough_time -= 1
        r, c = counter_terrorist
        step_r, step_c = maper[command]
        new_r, new_c = r + step_r, c + step_c
        if 0 <= new_r < n and 0 <= new_c < m:
            counter_terrorist = (new_r, new_c)
            if (new_r, new_c) == bomb:
                on_bomb = True
                continue
            elif (new_r, new_c) in terrorist:
                field_mat[new_r][new_c] = "*"
                counter_terrorist = None
                break
            on_bomb = False
    elif command == "defuse" and on_bomb:
        enough_time -= 4
        r, c = bomb
        if enough_time >= 0:
            field_mat[r][c] = "D"
            bomb = None
        else:
            field_mat[r][c] = "X"
            counter_terrorist = None
            bomb = None
        break
    elif command == "defuse" and not on_bomb:
        enough_time -= 2

    if enough_time <= 0:
        bomb = None
        counter_terrorist = None
        break

if not bomb and not counter_terrorist:
    print("Terrorists win!")
    print("Bomb was not defused successfully!")
    print(f"Time needed: {abs(enough_time)} second/s.")
elif not bomb and counter_terrorist:
    print("Counter-terrorist wins!")
    print(f"Bomb has been defused: {enough_time} second/s remaining.")
elif bomb and not counter_terrorist:
    print("Terrorists win!")

for row in field_mat:
    print(''.join(r for r in row))


