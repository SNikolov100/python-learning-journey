directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
}

def move_in_direction(start_point, direct_command):
    r, c = start_point
    dr, dc = directions[direct_command]
    return r + dr, c + dc

def is_valid_index(r, c, number):
    return 0 <= r < n and 0 <= c < number

def take_index_depend_conditions(r, c, num_of_stars, is_obstacles, position_player ):
    if (r, c) in is_obstacles:
        num_of_stars -= 1
        r, c = position_player
        return r, c, num_of_stars
    return r, c, num_of_stars

def is_star(r, c, num_of_stars, stars_set):
    num_of_stars += 1
    field_matr[r][c] = "."
    stars_set.remove((r, c))
    return stars_set, num_of_stars

n = int(input())
field_matr = []
player = None
stars = set()
obstacles = set()
number_of_stars = 2


for row in range(n):
    field_matr.append(input().split())
    for col in range(n):
        if field_matr[row][col] == "P":
            player = (row, col)
            field_matr[row][col] = "."
        elif field_matr[row][col] == "*":
            stars.add((row, col))
        elif field_matr[row][col] == "#":
            obstacles.add((row,col))

while True:
    command = input()
    row, col = move_in_direction(player, command)
    if is_valid_index(row, col, n):

        if (row, col) in stars:
            stars, number_of_stars = is_star(row, col, number_of_stars, stars)
        else:
            row, col, number_of_stars = take_index_depend_conditions(row, col, number_of_stars, obstacles, player)

    else:
        row, col = 0, 0
        if (0,0) in stars:
            stars, number_of_stars = is_star(row, col, number_of_stars, stars)
        else:
            row, col, number_of_stars = take_index_depend_conditions(row, col, number_of_stars, obstacles, player)
    player = (row, col)

    if number_of_stars == 10:
        print("You won! You have collected 10 stars.")
        break
    elif number_of_stars == 0:
        print("Game over! You are out of any stars.")
        break

r_last, c_last = player
field_matr[r_last][c_last] = "P"
print(f"Your final position is [{r_last}, {c_last}]")

for row in field_matr:
    print(f"{' '.join(x for x in row)}")


