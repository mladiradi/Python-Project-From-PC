
budget = float(input())
num_serials = int(input())

price = 0

for i in range(num_serials):
    text = input()
    price = float(input())

    if text == 'Thrones':
        price *= 0.5
    elif text == 'Lucifer':
        price *= 0.6
    elif text == 'Protector':
        price *= 0.7
    elif text == 'TotalDrama':
        price *= 0.8
    elif text == 'Area':
        price *= 0.9

    budget -= price

if budget >= 0:
    print(f"You bought all the series and left with {budget:.2f} lv.")
else:
    print(f"You need {abs(budget):.2f} lv. more to buy the series!")
