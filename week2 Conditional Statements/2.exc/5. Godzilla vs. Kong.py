budget = float(input())
walkon_n = int(input())
clotes_p = float(input())

decor = budget * (1 - 0.9)
clotes_total = walkon_n * clotes_p

if walkon_n > 150:
    clotes_total = clotes_total * (1 - 0.1)

needed_m = clotes_total + decor
left_m = budget - needed_m

if needed_m <= budget:
    print('Action!')
    print(f'Wingard starts filming with {left_m:.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {needed_m - budget:.2f} leva more.')
