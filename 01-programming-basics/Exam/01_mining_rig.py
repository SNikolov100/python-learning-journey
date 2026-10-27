from math import ceil
PRICE_OTHER_COMPONENT =1000
video_card = int(input())
transition = int(input())
current_per_card = float(input())
profit_card = float(input())

price_video_card = video_card * 13
price_transition = transition * 13
total_price = PRICE_OTHER_COMPONENT + price_video_card + price_transition
profit_card_per_day = profit_card - current_per_card

total_profit_card = 13 * profit_card_per_day
result = ceil(total_price / total_profit_card)

print(total_price)
print(result)
