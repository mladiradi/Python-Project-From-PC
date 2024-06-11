
coffee = 1.5
water = 1.0
coke = 1.4
snacks = 2.0


def orders(product, quantity) -> float:
    if product == 'coffee':
        return coffee * quantity
    elif product == 'water':
        return water * quantity
    elif product == 'coke':
        return coke * quantity
    return snacks * quantity


product_name = input()
product_quantity = float(input())

result = orders(product_name, product_quantity)
print(f'{result:.2f}')
