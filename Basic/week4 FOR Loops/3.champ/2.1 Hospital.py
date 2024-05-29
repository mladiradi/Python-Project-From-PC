period = int(input())

doctors = 7
reviewed = 0
non_reviewed = 0

for i in range(1, period + 1):
    patients_num = int(input())

    if i % 3 == 0 and non_reviewed > reviewed:
        doctors += 1

    if patients_num <= doctors:
        reviewed += patients_num
    else:
        non_reviewed += patients_num - doctors
        reviewed += abs(patients_num - (patients_num - doctors))

print(f'Treated patients: {reviewed}.')
print(f'Untreated patients: {non_reviewed}.')
