
budget = int(input())
destiny = input()
season = input()
days = int(input())

price = 0

if destiny == 'Dubai':
    if season == 'Winter':
        price = 45000
    else:
        price = 40000
    price *= 0.7
elif destiny == 'Sofia':
    if season == 'Winter':
        price = 17000
    else:
        price = 12500
    price *= 1.25
else:
    if season == 'Winter':
        price = 24000
    else:
        price = 20250

total = price * days
money = abs(budget - total)

if budget >= total:
    print(f"The budget for the movie is enough! We have {money:.2f} leva left!")
else:
    print(f"The director needs {money:.2f} leva more!")
