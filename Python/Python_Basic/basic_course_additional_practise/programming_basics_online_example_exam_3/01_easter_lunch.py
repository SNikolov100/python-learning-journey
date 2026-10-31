KOZUNAK = 3.20
EGGS = 4.35
COOKIES = 5.40
PAINT_EGGS = 0.15

number_kozunak = int(input())
number_eggs = int(input())
kg_cookies = int(input())

sum_kozunak = number_kozunak * KOZUNAK
sum_eggs = number_eggs * EGGS
sum_cookies = kg_cookies * COOKIES
price_paint = number_eggs * 12 * PAINT_EGGS

total_sum = sum_kozunak + sum_eggs + sum_cookies + price_paint

print(f"{total_sum:.2f}")
