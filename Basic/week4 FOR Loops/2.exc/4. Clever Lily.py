age_lili = int(input())
wash_price = float(input())
toy_price = int(input())

money = 0
sum_money = 0
toy = 0
counter = 0

for i in range(1, age_lili + 1):
    if i % 2 == 0:
        money += 10
        sum_money += money
        counter += 1
    else:
        toy += 1

toy_profit = toy * toy_price
toy_profit = toy_profit - counter  # after brother robbery
total_cash = toy_profit + sum_money
left = abs(total_cash - wash_price)

if total_cash >= wash_price:
    print(f'Yes! {left:.2f}')
else:
    print(f'No! {left:.2f}')
