from collections import deque

rows, cols = [int(x) for x in input().split()]
snake = deque(input())
my_matrix = [[] for _ in range(rows)]

for row in range(rows):
    if row % 2 == 0:
        for col in range(cols):
            my_matrix[row].append(snake[0])
            snake.rotate(-1)
    else:
        for col in range(cols):
            my_matrix[row].insert(0, snake[0])
            snake.rotate(-1)

# for row in my_matrix:
#     print(*row, sep="")
[print(*row, sep="") for row in my_matrix]

