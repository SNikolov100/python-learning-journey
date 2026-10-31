n = int(input())
wonderland = []
alice_position = None
rabit_hole = None
collect_tea = 0
game_over = False
direction = {
    "up": (-1,0),
    "down": (1,0),
    "left": (0,-1),
    "right": (0,1)
}
for row in range(n):
    wonderland.append(input().split())
    for col in range(n):
        if wonderland[row][col] == "A":
            alice_position = (row, col)
        elif wonderland[row][col] == "R":
            rabit_hole = (row, col)

while True:
    command = input()
    r, c = alice_position
    wonderland[r][c] = "*"
    add_row, add_coll = direction[command]
    new_r = r + add_row
    new_c = c + add_coll
    if 0<= new_r < n and 0<= new_c < n:
        if wonderland[new_r][new_c] == "R":
            wonderland[new_r][new_c] = "*"
            game_over = True
            break
        alice_position = (new_r, new_c)
        if wonderland[new_r][new_c] != "." and wonderland[new_r][new_c] != "*":
            collect_tea += int(wonderland[new_r][new_c])
    else:
        game_over = True
        break
    if collect_tea >= 10:
        wonderland[new_r][new_c] = "*"
        break


if game_over:
    print(f"Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")
for row in wonderland:
    print(*row)
