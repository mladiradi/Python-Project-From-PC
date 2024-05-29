
budget = float(input())

counter_total = 0
total_price = 0
counter = 1

while True:
    text = str.lower(input())
    if text == "stop":
        print(f"You bought {counter_total} products for {total_price:.2f} leva.")
        break
    price = float(input())
    if counter == 3:
        price /= 2
        counter = 0
    total_price += price
    if price > budget:
        print(f"You don't have enough money!")
        print(f"You need {price - budget:.2f} leva!")
        break
    budget -= price
    counter_total += 1
    counter += 1
