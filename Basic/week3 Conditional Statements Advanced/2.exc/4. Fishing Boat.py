budg = int(input())
seas = input()
mans = int(input())

price = 0
total = 0

if mans <= 6:
    if seas == 'Summer' or seas == 'Autumn':
        price = 4200 * 0.9
    elif seas == 'Spring':
        price = 3000 * 0.9
    elif seas == 'Winter':
        price = 2600 * 0.9
elif 7 <= mans <= 11:
    if seas == 'Summer' or seas == 'Autumn':
        price = 4200 * 0.85
    elif seas == 'Spring':
        price = 3000 * 0.85
    elif seas == 'Winter':
        price = 2600 * 0.85
else:
    if seas == 'Summer' or seas == 'Autumn':
        price = 4200 * 0.75
    elif seas == 'Spring':
        price = 3000 * 0.75
    elif seas == 'Winter':
        price = 2600 * 0.75

if mans % 2 == 0 and seas != 'Autumn':
    price *= 0.95

total = abs(budg - price)

if budg >= price:
    print(f'Yes! You have {total:.2f} leva left.')
else:
    print(f'Not enough money! You need {total:.2f} leva.')
