days = int(input())
every_3_days = 0
untreated_patients = 0
treated_patients = 0
doctors = 7

for every_3_days in range(1, days + 1):
    count_patient = int(input())
    if (every_3_days % 3) == 0:

        if untreated_patients > treated_patients:
            doctors += 1

    if count_patient > doctors:
        untreated_patients += count_patient - doctors
        treated_patients += doctors
    else:
        treated_patients += count_patient

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")



