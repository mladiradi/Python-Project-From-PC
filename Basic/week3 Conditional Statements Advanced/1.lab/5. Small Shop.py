prod = input()
town = input()
quan = float(input())

price = 0

if town == 'Sofia':
    if prod == 'coffee':
        price = 0.5
    elif prod == 'water':
        price = 0.8
    elif prod == 'beer':
        price = 1.2
    elif prod == 'sweets':
        price = 1.45
    elif prod == 'peanuts':
        price = 1.6
elif town == 'Plovdiv':
    if prod == 'coffee':
        price = 0.4
    elif prod == 'water':
        price = 0.7
    elif prod == 'beer':
        price = 1.15
    elif prod == 'sweets':
        price = 1.3
    elif prod == 'peanuts':
        price = 1.5
elif town == 'Varna':
    if prod == 'coffee':
        price = 0.45
    elif prod == 'water':
        price = 0.7
    elif prod == 'beer':
        price = 1.1
    elif prod == 'sweets':
        price = 1.35
    elif prod == 'peanuts':
        price = 1.55

print(price * quan)
