
stock = {}
sold = 0
while True:
    text = input()
    if text == "Complete":
        break
    parts = text.split()
    command, quantity, food_name = parts[0], int(parts[1]), parts[2]

    if command == "Receive":
        if quantity > 0:
            if food_name in stock:
                stock[food_name] += quantity
            else:
                stock[food_name] = quantity

    elif command == "Sell":
        if food_name not in stock:
            print(f"You do not have any {food_name}.")
        elif quantity > stock[food_name]:
            sold += stock[food_name]
            print(f"There aren't enough {food_name}. You sold the last {stock[food_name]} of them.")
            del stock[food_name]
        else:
            stock[food_name] -= quantity
            sold += quantity
            print(f"You sold {quantity} {food_name}.")
            if stock[food_name] == 0:
                del stock[food_name]

for food_name, quantity in stock.items():
    print(f"{food_name}: {quantity}")

print(f"All sold: {sold} goods")
