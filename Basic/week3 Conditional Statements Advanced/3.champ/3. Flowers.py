chry_num = int(input())
rose_num = int(input())
tuli_num = int(input())
season = input()
holyday = input()

chry_price = 0
rose_price = 0
tuli_price = 0
sume = 0

if season == 'Spring' or season == 'Summer':
    chry_price = chry_num * 2.0
    rose_price = rose_num * 4.1
    tuli_price = tuli_num * 2.5
    sume = chry_price + rose_price + tuli_price
    if holyday == 'Y':
        sume *= 1.15
elif season == 'Autumn' or season == 'Winter':
    chry_price = chry_num * 3.75
    rose_price = rose_num * 4.5
    tuli_price = tuli_num * 4.15
    sume = chry_price + rose_price + tuli_price
    if holyday == 'Y':
        sume *= 1.15

if season == 'Spring' and tuli_num > 7:
    sume *= 0.95

if season == 'Winter' and rose_num >= 10:
    sume *= 0.9

if (chry_num + rose_num + tuli_num) > 20:
    sume *= 0.8

print(f'{sume + 2:.2f}')
