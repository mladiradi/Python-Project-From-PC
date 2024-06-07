lst_of_purchase = input().split("|")
budget = float(input())

ticket_price = 150
profit = 0
sum_selling_price = 0

for i in lst_of_purchase:
    splitter = i.split("->")
    item = splitter[0]
    price_item = float(splitter[1])

    if (item == "Clothes" and price_item > 50.00) or \
            (item == "Shoes" and price_item > 35.00) or \
            (item == "Accessories" and price_item > 20.50):
        continue

    if budget >= price_item:
        budget -= price_item
        selling_p = price_item * 1.4
        profit += selling_p - price_item
        sum_selling_price += selling_p
        print(f'{selling_p:.2f}', end=" ")
    else:
        continue
print()
print(f"Profit: {abs(profit):.2f}")

if sum_selling_price + budget > ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")
