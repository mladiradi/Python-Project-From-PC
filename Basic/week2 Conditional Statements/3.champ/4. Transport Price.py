km = int(input())
daytime = input()

if km < 20 and daytime == 'day':
    price = km * 0.79 + 0.7
    print(f'{price:.2f}')
elif km < 20 and daytime == 'night':
    price = km * 0.9 + 0.7
    print(f'{price:.2f}')
elif 20 <= km < 100:
    price = km * 0.09
    print(f'{price:.2f}')
elif km >= 100:
    price = km * 0.06
    print(f'{price:.2f}')

#print(f'{price:.2f}')
