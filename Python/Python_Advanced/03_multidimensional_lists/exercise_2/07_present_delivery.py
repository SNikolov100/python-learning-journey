move_santa = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
}
present_n = int(input())
n_matr = int(input())
santa_matrix = []
position_santa = ()
nice_kids = set()
naughty_kids = set()
cookies = set()
no_present = False

for row in range(n_matr):
    santa_matrix.append(input().split())
    for col in range(n_matr):
        if santa_matrix[row][col] == "S":
            position_santa = (row, col)
            santa_matrix[row][col] = "-"
        elif santa_matrix[row][col] == "V":
            nice_kids.add((row, col))
        elif santa_matrix[row][col] == "X":
            naughty_kids.add((row, col))
        elif santa_matrix[row][col] == "C":
            cookies.add((row, col))
count_nice_kids = len(nice_kids)

while True:
    command = input()
    if command == "Christmas morning":
        break
    r, c = position_santa
    new_r, new_c = r + move_santa[command][0], c + move_santa[command][1]
    if 0 <= new_r < n_matr and 0 <= new_c < n_matr:
        if (new_r, new_c) in nice_kids:
            present_n -= 1
            nice_kids.remove((new_r,new_c))
        elif santa_matrix[new_r][new_c] == "C":
            for direct in move_santa:
                d_r, d_c = new_r + move_santa[direct][0], new_c + move_santa[direct][1]
                if 0 <= d_r < n_matr and 0 <= d_c < n_matr:
                    if (d_r, d_c) in nice_kids:
                        nice_kids.remove((d_r, d_c))
                        present_n -= 1
                    elif (d_r, d_c) in naughty_kids:
                        present_n -= 1
                        naughty_kids.remove((d_r, d_c))
                    santa_matrix[d_r][d_c] = "-"
                    if present_n == 0:
                        break

        santa_matrix[new_r][new_c] = "S"
        santa_matrix[r][c] = "-"
        position_santa = (new_r, new_c)
    if present_n == 0:
        no_present = True
        break
if no_present and nice_kids:
    print("Santa ran out of presents!")
for data in santa_matrix:
    print(*data)
if not nice_kids:
    print(f"Good job, Santa! {count_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {len(nice_kids)} nice kid/s.")

