products_quantity = {}
product_price = {}

while True:
    data = input().split(" ")
    if "buy" in data:
        break

    name, price, quantity = data[0], float(data[1]), int(data[2])
    if name not in product_price.keys():
        products_quantity[name] = 0
        product_price[name] = 0.0
    products_quantity[name] += quantity
    product_price[name] = price

for key, value in products_quantity.items():
    price = value * product_price[key]
    print(f"{key} -> {price:.2f}")


# dictionary = {key: value for (key, value) in data}

# # input:
#
# Beer 2.20 100
# IceTea 1.50 50
# NukaCola 3.30 80
# Water 1.00 500
# buy

# # result:
#
# Beer -> 220.00
# IceTea -> 75.00
# NukaCola -> 264.00
# Water -> 500.00

# Beer 2.40 350
# IceTea 5.20 100
# Beer 1.20 200
# IceTea 0.50 120
# buy


# line = input().split(" ")
# productQuantity = {}
# productPrices = {}
#
# while "buy" not in line:
#     product = line[0]
#     price = float(line[1])
#     quantity = int(line[2])
#
#     if product not in productQuantity.keys():
#         productQuantity[product] = 0
#         productPrices[product] = 0.00
#     productQuantity[product] += quantity
#     productPrices[product] = price
#     line = input().split(" ")
#
#     if "buy" in line:
#         break
#
# for key, value in productQuantity.items():
#     price = value * productPrices[key]
#     print(f"{key} -> {price:.2f}")
