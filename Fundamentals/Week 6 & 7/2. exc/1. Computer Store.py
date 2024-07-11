
sum_price = 0
total_price = 0

while True:
    text = input()
    if text == "special" or text == "regular":
        break

    price = float(text)
    if price < 0:
        print("Invalid price!")
    else:
        sum_price += price

tax = sum_price * 0.2
total_price = sum_price + tax
if text == 'special':
    total_price *= 0.9
if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {sum_price:.2f}$")
    print(f"Taxes: {tax:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")
