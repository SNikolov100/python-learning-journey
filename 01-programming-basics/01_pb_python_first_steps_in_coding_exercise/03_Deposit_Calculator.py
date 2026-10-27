deposit_amount = float(input())
months_for_deposit = int(input())
interest_rate = float(input()) / 100

rate = deposit_amount * interest_rate
rate_for_month = rate /12
amount = deposit_amount + \
         rate_for_month * \
         months_for_deposit

print (amount)