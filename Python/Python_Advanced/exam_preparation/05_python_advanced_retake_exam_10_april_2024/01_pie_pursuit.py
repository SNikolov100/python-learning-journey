from collections import deque

contestants = deque(int(x) for x in input().split())
pies = [int(x) for x in input().split()]

while contestants and pies:
    contest = contestants.popleft()
    piece_of_pie = pies.pop()

    if contest >= piece_of_pie:
        contest -= piece_of_pie
        if contest > 0:
            contestants.append(contest)
    else:
        piece_of_pie -= contest
        if piece_of_pie == 1 and len(pies) > 1:
            pies[-1] += piece_of_pie
        elif piece_of_pie == 1 and len(pies) == 1:
            pies.append(piece_of_pie)
        else:
            pies.append(piece_of_pie)

if not pies and contestants:
    print("We will have to wait for more pies to be baked!")
    print(f"Contestants left: {', '.join(str(x) for x in contestants)}")
elif not pies and not contestants:
    print("We have a champion!")
elif pies and not contestants:
    print("Our contestants need to rest!")
    print(f"Pies left: {', '.join(str(x) for x in pies)}")

