
stock = {}

while True:
    command = input()
    if command == "statistics":
        break

    product, quantity = command.split(": ")
    quantity = int(quantity)

    if product in stock:
        stock[product] += quantity
    else:
        stock[product] = quantity

counter = len(stock)
total_quantity = sum(stock.values())

print(f"Products in stock:")
for product, quantity in stock.items():
    print(f"- {product}: {quantity}")
    # [print(f"- {product}: {quantity}") for product, quantity in products]
print(f"Total Products: {counter}")
print(f"Total Quantity: {total_quantity}")


# # input:
#
# bread: 4
# cheese: 2
# ham: 1
# bread: 1
# statistics

# # result:
#
# Products in stock:
# - bread: 5
# - cheese: 2
# - ham: 1
# Total Products: 3
# Total Quantity: 8
