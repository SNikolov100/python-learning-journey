
def hit_knights(knights_list, chest_board_matrix):
    position_for_move = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))
    remove_knights = 0
    knight_set = set(tuple(x) for x in knights_list)
    while True:
        max_hits = 0
        max_knight = None
        for knight in knights_list:
            r, c = knight
            temp_hits = 0
            for position in position_for_move:
                new_r, new_c = r + position[0] , c + position[1]
                if 0 <= new_r < len(chest_board_matrix) and 0 <= new_c < len(chest_board_matrix[0]):
                    if (new_r, new_c) in knight_set:
                        temp_hits +=1
            if temp_hits > max_hits:
                max_hits = temp_hits
                max_knight = (r, c)
        if max_hits == 0:
            break
        del_r, del_c = max_knight
        knights_list.remove([del_r, del_c])
        knight_set.remove((del_r,del_c))
        remove_knights += 1
    return remove_knights



chest_board = []
knights = []
for row in range(int(input())):
    chest_board.append([x for x in input()])
    for col in range(len(chest_board[0])):
        if chest_board[row][col] == "K":
            knights.append([row, col])

del_knights = hit_knights(knights, chest_board)
print(del_knights)