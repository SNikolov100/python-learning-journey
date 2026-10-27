days = int(input())
total_tax = 0
hours = int(input())

for day in range(1, days + 1):
    tax_parking = 0
    for hour in range(1, hours + 1):
        if (day % 2 == 0) and (hour % 2 != 0):
            tax_parking += 2.5
        elif (day % 2 != 0) and (hour % 2 == 0):
            tax_parking += 1.25
        else:
            tax_parking += 1
    print(f"Day: {day} - {tax_parking:.2f} leva")
    total_tax += tax_parking
print(f"Total: {total_tax:.2f} leva")