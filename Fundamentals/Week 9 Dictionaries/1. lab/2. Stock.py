
element = input().split()
products = input().split()
stock = {}

for i in range(0, len(element), 2):
    key = element[i]
    value = element[i + 1]
    stock[key] = int(value)

for product in products:
    if product in stock.keys():  # или само stock
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

# cheese 10 bread 5 ham 10 chocolate 3
# jam cheese ham tomatoes

# result =
# Sorry, we don't have jam
# We have 10 of cheese left
# We have 10 of ham left
# Sorry, we don't have tomatoes
