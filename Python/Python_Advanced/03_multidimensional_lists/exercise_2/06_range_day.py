def action_function(comm, shoot_matrix, position, target, hit_targ):

    action_command, heading = comm[0], comm[1]
    pos_row, pos_col = position
    bull_row, bull_col = position
    if action_command == "move":
        shoot_matrix[pos_row][pos_col] = "."
        for steps in range(int(comm[2])):
            pos_row += direction[heading][0]
            pos_col += direction[heading][1]
            if 0<= pos_row < NUMBER and 0<= pos_col < NUMBER:
                if shoot_matrix[pos_row][pos_col] == ".":
                    position = (pos_row, pos_col)
            else:
                break
        return position, hit_targ
    elif action_command == "shoot":
        while True:
            r, c = direction[heading]
            bull_row += r
            bull_col += c
            if 0 <= bull_row < NUMBER and 0 <= bull_col < NUMBER:
                if shoot_matrix[bull_row][bull_col] == "x":
                    shoot_matrix[bull_row][bull_col] = "."
                    hit_targ.append([bull_row,bull_col])
                    target.remove((bull_row, bull_col))
                    break
            else:
                break
    return position, hit_targ

direction = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }
NUMBER = 5
shoot_area = []
my_position = ()
targets = set()
hit_target = []

for row in range(NUMBER):
    shoot_area.append(input().split())
    for col in range(NUMBER):
        if shoot_area[row][col] == "A":
            my_position = (row, col)
        elif shoot_area[row][col] == "x":
            targets.add((row, col))
count_targets = len(targets)
lines = int(input())

for _ in range(lines):
    commands = input().split()
    my_position, hit_target = action_function(commands, shoot_area, my_position, targets, hit_target)
    if not targets:
        print(f"Training completed! All {count_targets} targets hit.")
        break

if targets:
    print(f"Training not completed! {len(targets)} targets left.")

if hit_target:
    for data in hit_target:
        print(data)