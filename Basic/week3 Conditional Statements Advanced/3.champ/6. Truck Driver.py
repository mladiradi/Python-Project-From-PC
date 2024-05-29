season = input()
km = float(input())

month_in_season = 4
income = 0.0
profit = 0.0

if season == 'Spring' or season == 'Autumn':
    if km <= 5000:
        income = km * 0.75
    elif 5000 < km <= 10000:
        income = km * 0.95
    else:
        income = km * 1.45
elif season == 'Summer':
    if km <= 5000:
        income = km * 0.9
    elif 5000 < km <= 10000:
        income = km * 1.1
    else:
        income = km * 1.45
elif season == 'Winter':
    if km <= 5000:
        income = km * 1.05
    elif 5000 < km <= 10000:
        income = km * 1.25
    else:
        income = km * 1.45

profit = (income * month_in_season) * 0.9

print(f'{profit:.2f}')
