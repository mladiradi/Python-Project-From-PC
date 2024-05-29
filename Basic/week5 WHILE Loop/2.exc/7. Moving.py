
a1 = int(input())
a2 = int(input())
a3 = int(input())

space = a1 * a2 * a3

while True:
    text = input()

    if text == 'Done' or space == 0:
        print(f"{space} Cubic meters left.")
        break

    box = int(text)
    space -= box

    if space < 0:
        print(f"No more free space! You need {abs(space)} Cubic meters more.")
        break
