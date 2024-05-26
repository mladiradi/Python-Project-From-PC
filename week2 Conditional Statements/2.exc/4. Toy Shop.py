price = float(input())
puzzel = int(input())
barbie = int(input())
bear = int(input())
minion = int(input())
truck = int(input())

count = puzzel + barbie + bear + minion + truck
suma = puzzel * 2.6 + barbie * 3 + bear * 4.10 + minion * 8.2 + truck * 2

if count >= 50:
    suma = suma * (1 - 0.25)

rent = suma * (1 - 0.1)

if rent >= price:
    print(f'Yes! {rent - price:.2f} lv left.')
else:
    print(f'Not enough money! {price - rent:.2f} lv needed.')
