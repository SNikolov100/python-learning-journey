target_high = int(input())
start_high = target_high - 30
is_fails = False
count_jumps = 0
is_success_target = False

while True:
    is_success_current_high = False

    for _ in range(3):
        count_jumps += 1
        current_high = int(input())

        if current_high > start_high:
            if start_high >= target_high:
                is_success_target = True
                break
            start_high += 5
            is_success_current_high = True
            break
    if is_success_target:
        break
    if not is_success_current_high:
        is_fails = True
        break

if is_fails:
    print(f"Tihomir failed at {start_high:.0f}cm after {count_jumps} jumps.")
else:
    print(f"Tihomir succeeded, he jumped over {start_high:.0f}cm after {count_jumps} jumps.")
