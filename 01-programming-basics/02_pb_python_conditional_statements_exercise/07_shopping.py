VIDEO_CARD_PRICE = 250
PROCESSOR_PERSENT = 0.35
RAM_PERSENT = 0.10
DISCOUNT = 0.15

budget = float(input())
number_video_cards = int(input())
number_processors = int(input())
number_ram = int(input())

price_one_processor = (number_video_cards * VIDEO_CARD_PRICE) * PROCESSOR_PERSENT
price_one_ram = (number_video_cards * VIDEO_CARD_PRICE) * RAM_PERSENT

price_sum = (number_video_cards * VIDEO_CARD_PRICE) + \
            (price_one_processor * number_processors) + \
            (price_one_ram * number_ram)
if number_video_cards > number_processors:
    price_sum -= price_sum * DISCOUNT

if price_sum <= budget:
    print(f"You have {abs(price_sum - budget):.2f} leva left!")
else:
    print(f"Not enough money! You need {abs(price_sum - budget):.2f} leva more!")