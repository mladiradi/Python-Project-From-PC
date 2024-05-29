period = int(input())

doctors = 7
reviewed = 0
non_reviewed = 0
sum_non_reviewed = 0

for i in range(1, period + 1):
    patients_num = int(input())

    if i % 3 == 0 and sum_non_reviewed > reviewed:
        doctors += 1

    if patients_num > doctors:
        non_reviewed = abs(patients_num - doctors)
        sum_non_reviewed += non_reviewed

    if patients_num >= doctors:
        reviewed += doctors
    else:
        reviewed += patients_num

print(f'Treated patients: {reviewed}.')
print(f'Untreated patients: {sum_non_reviewed}.')
