budg = float(input())
seas = input()

if budg <= 100:
    if seas == 'summer':
        budg *= 0.3
        print('Somewhere in Bulgaria')
        print(f'Camp - {budg:.2f}')
    elif seas == 'winter':
        budg *= 0.7
        print('Somewhere in Bulgaria')
        print(f'Hotel - {budg:.2f}')

elif 100 < budg <= 1000:
    if seas == 'summer':
        budg *= 0.4
        print('Somewhere in Balkans')
        print(f'Camp - {budg:.2f}')
    elif seas == 'winter':
        budg *= 0.8
        print('Somewhere in Balkans')
        print(f'Hotel - {budg:.2f}')
else:
    budg *= 0.9
    print('Somewhere in Europe')
    print(f'Hotel - {budg:.2f}')
