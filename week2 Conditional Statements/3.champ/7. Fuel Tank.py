type_f = (input())
fuel_l = float(input())

types = str.lower(type_f)

if types == 'gas' or types == 'diesel' or types == 'gasoline':
    if fuel_l >= 25:
        print(f'You have enough {types}.')
    elif fuel_l < 25:
        print(f'Fill your tank with {types}!')
else:
    print("Invalid fuel!")
