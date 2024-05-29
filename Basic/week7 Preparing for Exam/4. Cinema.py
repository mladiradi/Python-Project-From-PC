
capacity = int(input())

price = 0
total = 0

while True:
    text = input()
    if text == 'Movie time!':
        print(f"There are {capacity} seats left in the cinema.")
        break

    num = int(text)
    capacity -= num
    price = num * 5

    if num % 3 == 0:
        price -= 5

    if capacity < 0:
        print("The cinema is full.")
        break
    total += price
print(f"Cinema income - {total} lv.")
