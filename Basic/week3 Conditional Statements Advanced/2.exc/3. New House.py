flow = input()
quan = int(input())
budg = int(input())

price = 0.0

if flow == 'Roses':
    price = 5.0 * quan
    if quan > 80:
        price *= 0.9
elif flow == 'Dahlias':
    price = 3.80 * quan
    if quan > 90:
        price *= 0.85
elif flow == 'Tulips':
    price = 2.80 * quan
    if quan > 80:
        price *= 0.85
elif flow == 'Narcissus':
    price = 3.0 * quan
    if quan < 120:
        price *= 1.15
elif flow == 'Gladiolus':
    price = 2.50 * quan
    if quan < 80:
        price *= 1.2

balance = abs(budg - price)

if budg >= price:
    print(f'Hey, you have a great garden with {quan} {flow} and {balance:.2f} leva left.')
else:
    print(f'Not enough money, you need {balance:.2f} leva more.')
