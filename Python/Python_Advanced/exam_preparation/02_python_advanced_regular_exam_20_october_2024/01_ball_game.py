from collections import deque
strength_kick = [int(x) for x in input().split()]
accuracy_kick = deque(int(x) for x in input().split())
total_score_goal = 0

while strength_kick and accuracy_kick:
    temp_strength = strength_kick[-1]
    temp_accuracy = accuracy_kick[0]
    result = temp_strength + temp_accuracy
    if result == 100:
        strength_kick.pop()
        accuracy_kick.popleft()
        total_score_goal += 1
    elif result < 100:
        if temp_strength < temp_accuracy:
            strength_kick.pop()
        elif temp_strength> temp_accuracy:
            accuracy_kick.popleft()
        elif temp_strength == temp_accuracy:
            accuracy_kick.popleft()
            strength_kick[-1] += temp_accuracy
    else:
        strength_kick[-1] -= 10
        accuracy_kick.rotate(-1)

if total_score_goal == 3:
    print("Paul scored a hat-trick!")
elif total_score_goal < 1:
    print("Paul failed to score a single goal.")
elif total_score_goal > 3:
    print("Paul performed remarkably well!")
elif 0 < total_score_goal < 3:
    print("Paul failed to make a hat-trick.")
if 0 < total_score_goal:
    print(f"Goals scored: {total_score_goal}")

if strength_kick:
    print(f"Strength values left: {', '.join(str(x) for x in strength_kick)}")
if accuracy_kick:
    print(f"Accuracy values left: {', '.join(str(x) for x in accuracy_kick)}")
