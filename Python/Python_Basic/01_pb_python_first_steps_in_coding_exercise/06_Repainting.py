NYLON_PRICE = 1.50
PAINT_PRICE = 14.50
THINNER_PRICE = 5.00
BACKS_PRICE = 0.40

nylon_m2 = int(input())
paint_litters = int(input())
thinner_litters = int(input())
work_hours = int(input())

price_nylon = (2 + nylon_m2) * NYLON_PRICE
paint_litters += paint_litters * 0.1
price_paint = paint_litters * PAINT_PRICE
price_thinner = thinner_litters * THINNER_PRICE

sum_all = BACKS_PRICE + price_nylon + price_paint + price_thinner
payment_worker = (sum_all * 0.3) * work_hours
total_result = sum_all + payment_worker

print(total_result)



