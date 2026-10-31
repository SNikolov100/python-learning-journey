number_days = int(input())
win_current_game = 0
earn_money = 0
win_day = 0
for _ in range(number_days):
    count_win = 0
    count_lose = 0
    win_current_game = 0
    while True:
        current_game = input()
        if current_game == "Finish":
            break
        result_current_game = input()

        if result_current_game == "win":
            count_win += 1
            win_current_game += 20
        elif result_current_game == "lose":
            count_lose += 1
    if count_win > count_lose:
        win_current_game += win_current_game * 0.1
        win_day += 1
    earn_money += win_current_game

if win_day > (number_days - win_day):
    earn_money += earn_money * 0.2
    print(f"You won the tournament! Total raised money: {earn_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {earn_money:.2f}")