budget = float(input())
season = input()

clazz = ''
types = ''
price = 0

if budget <= 100:
    clazz = 'Economy class'
    if season == 'Summer':
        budget *= 0.35
        types = 'Cabrio'
    elif season == 'Winter':
        budget *= 0.65
        types = 'Jeep'
elif 100 < budget <= 500:
    clazz = 'Compact class'
    if season == 'Summer':
        budget *= 0.45
        types = 'Cabrio'
    elif season == 'Winter':
        budget *= 0.8
        types = 'Jeep'
elif budget > 500:
    clazz = 'Luxury class'
    budget *= 0.9
    types = 'Jeep'

print(clazz)
print(f"{types} - {budget:.2f}")
