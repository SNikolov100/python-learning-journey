PRICE_TOY = 5
PRICE_SWEATER = 15
count_adults = 0
count_kids = 0

while True:
    age_member_family_str = input()
    if age_member_family_str == "Christmas":
        break
    age_member_family_int = int(age_member_family_str)

    if age_member_family_int > 16:
        count_adults += 1
    else:
        count_kids += 1

money_for_adults = count_adults * PRICE_SWEATER
money_for_kids = count_kids * PRICE_TOY

print(f"Number of adults: {count_adults}")
print(f"Number of kids: {count_kids}")
print(f"Money for toys: {money_for_kids}")
print(f"Money for sweaters: {money_for_adults}")