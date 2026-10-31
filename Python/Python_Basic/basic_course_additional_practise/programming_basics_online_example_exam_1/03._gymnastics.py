RUSSIA_RIBBON_DIFFICULT = 9.1
RUSSIA_RIBBON_PERFORMANCE = 9.4
RUSSIA_HOOP_DIFFICULT = 9.3
RUSSIA_HOOP_PERFORMANCE = 9.8
RUSSIA_ROPE_DIFFICULT = 9.6
RUSSIA_ROPE_PERFORMANCE = 9.0
BULGARIA_RIBBON_DIFFICULT = 9.6
BULGARIA_RIBBON_PERFORMANCE = 9.4
BULGARIA_HOOP_DIFFICULT = 9.55
BULGARIA_HOOP_PERFORMANCE = 9.75
BULGARIA_ROPE_DIFFICULT = 9.5
BULGARIA_ROPE_PERFORMANCE = 9.4
ITALY_RIBBON_DIFFICULT = 9.2
ITALY_RIBBON_PERFORMANCE = 9.5
ITALY_HOOP_DIFFICULT = 9.45
ITALY_HOOP_PERFORMANCE = 9.35
ITALY_ROPE_DIFFICULT = 9.7
ITALY_ROPE_PERFORMANCE = 9.15

sum_points = 0

country = input()
tools = input()

if country == "Russia":
    if tools == "ribbon":
        sum_points = RUSSIA_RIBBON_DIFFICULT + RUSSIA_RIBBON_PERFORMANCE
    elif tools == "hoop":
        sum_points = RUSSIA_HOOP_DIFFICULT + RUSSIA_HOOP_PERFORMANCE
    elif tools == "rope":
        sum_points = RUSSIA_ROPE_DIFFICULT + RUSSIA_ROPE_PERFORMANCE
if country == "Bulgaria":
    if tools == "ribbon":
        sum_points = BULGARIA_RIBBON_DIFFICULT + BULGARIA_RIBBON_PERFORMANCE
    elif tools == "hoop":
        sum_points = BULGARIA_HOOP_DIFFICULT + BULGARIA_HOOP_PERFORMANCE
    elif tools == "rope":
        sum_points = BULGARIA_ROPE_DIFFICULT + BULGARIA_ROPE_PERFORMANCE
if country == "Italy":
    if tools == "ribbon":
        sum_points = ITALY_RIBBON_DIFFICULT + ITALY_RIBBON_PERFORMANCE
    elif tools == "hoop":
        sum_points = ITALY_HOOP_DIFFICULT + ITALY_HOOP_PERFORMANCE
    elif tools == "rope":
        sum_points = ITALY_ROPE_DIFFICULT + ITALY_ROPE_PERFORMANCE

print(f"The team of {country} get {sum_points:.3f} on {tools}.")
print(f"{100 - (sum_points * 100)/20:.2f}%")