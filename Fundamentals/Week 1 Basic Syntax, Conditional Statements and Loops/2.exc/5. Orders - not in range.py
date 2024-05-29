
number_of_orders = int(input())

total_price = 0

for orders in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if not 0.01 <= price_per_capsule <= 100.00:
        continue
    elif days not in range(1, 31 + 1):
        continue
    elif capsules_per_day not in range(1, 2000 + 1):
        continue

    day_price = price_per_capsule * days * capsules_per_day
    total_price += day_price

    print(f"The price for the coffee is: ${day_price:.2f}")

print(f"Total: ${total_price:.2f}")

# if 0.01 > price_per_capsule or price_per_capsule > 100.00:
#   continue
