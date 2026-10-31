from collections import deque

worms = [int(x) for x in input().split()]
holes = deque(int(x) for x in input().split())
matches_counter= 0
all_worms_not_matches = False

while worms and holes:
    last_worm = worms.pop()
    first_hole = holes.popleft()
    if last_worm == first_hole:
        matches_counter += 1
        continue
    last_worm -= 3
    if last_worm > 0:
        worms.append(last_worm)
    else:
        all_worms_not_matches = True

if matches_counter > 0:
    print(f"Matches: {matches_counter}")
else:
    print("There are no matches.")

if not worms and not all_worms_not_matches:
    print("Every worm found a suitable hole!")
elif not worms and all_worms_not_matches:
    print("Worms left: none")
elif worms:
    print(f"Worms left: {', '.join(str(x) for x in worms)}")

if not holes:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join(str(x) for x in holes)}")

