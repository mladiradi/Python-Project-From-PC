
num_joi = int(input())
type_joi = input()
delivery = input()

if type_joi == '90X130':
    price = 110
    if num_joi > 60:
        price *= 0.92
    elif num_joi > 30:
        price *= 0.95
elif type_joi == '100X150':
    price = 140
    if num_joi > 80:
        price *= 0.9
    elif num_joi > 40:
        price *= 0.94
elif type_joi == '130X180':
    price = 190
    if num_joi > 50:
        price *= 0.88
    elif num_joi > 20:
        price *= 0.93
else:
    price = 250
    if num_joi > 50:
        price *= 0.86
    elif num_joi > 25:
        price *= 0.91

total = num_joi * price

if delivery == 'With delivery':
    total += 60

if num_joi < 10:
    print('Invalid order')
elif num_joi > 99:
    total *= 0.96
    print(f'{total:.2f} BGN')
else:
    print(f'{total:.2f} BGN')
