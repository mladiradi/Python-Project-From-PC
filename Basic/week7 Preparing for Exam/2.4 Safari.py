
budget = float(input())
lt_need = float(input())
day_of_week = input()

price = (lt_need * 2.1) + 100

if day_of_week == "Saturday":
    price *= 0.9
elif day_of_week == "Sunday":
    price *= 0.8

if budget >= price:
    print(f"Safari time! Money left: {budget - price:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {price - budget:.2f} lv.")
