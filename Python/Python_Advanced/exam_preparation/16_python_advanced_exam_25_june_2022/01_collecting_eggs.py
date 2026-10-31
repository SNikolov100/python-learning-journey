from collections import deque
egg_size = deque(int(x) for x in input().split(", "))
piece_of_paper = [int(x) for x in input().split(", ")]
box = 0

while egg_size and piece_of_paper:
    first_egg = egg_size.popleft()
    if first_egg <= 0 :
        continue
    if first_egg == 13:
        piece_of_paper = [piece_of_paper[-1]] + piece_of_paper[1:-1] + piece_of_paper[0:1]
        continue
    last_paper = piece_of_paper.pop()
    sum_size = first_egg + last_paper
    if sum_size <= 50:
        box += 1

if box > 0:
    print(f"Great! You filled {box} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if egg_size:
    print(f"Eggs left: {', '.join(str(x) for x in egg_size)}")
if piece_of_paper:
    print(f"Pieces of paper left: {', '.join(str(x) for x in piece_of_paper)}")

