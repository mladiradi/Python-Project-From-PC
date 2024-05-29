
pr_lug_over_20kg = float(input())
kg_lug = float(input())
day_to_travel = int(input())
num_lug = int(input())

if kg_lug < 10:
    price = pr_lug_over_20kg * 0.2
elif kg_lug <= 20:
    price = pr_lug_over_20kg * 0.5
else:
    price = pr_lug_over_20kg

if day_to_travel < 7:
    price *= 1.4
elif day_to_travel <= 30:
    price *= 1.15
else:
    price *= 1.1

total = num_lug * price

print(f"The total price of bags is: {total:.2f} lv. ")
