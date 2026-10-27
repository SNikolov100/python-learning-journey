YEARS_IVAN = 18
YEARS_START = 1800

inherit_money = float(input())
last_year_for_life = int(input())

years_even = 0
years_odd = 0
spend_money = 0

for years_count in range(YEARS_START,last_year_for_life+1):
    if (years_count % 2) == 0:
        spend_money += 12000
        years_even += 1
    else:
        years_odd += 1
        spend_money += 12000 + (50 * (years_count - YEARS_START + YEARS_IVAN))

left_money = inherit_money - spend_money

if left_money >= 0:
    print(f"Yes! He will live a carefree life and will have {left_money:.2f} dollars left.")
else:
    print(f"He will need {abs(left_money):.2f} dollars to survive.")

