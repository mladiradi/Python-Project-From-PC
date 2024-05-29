
a = int(input())
b = int(input())

cake_pieces = a * b

while True:
    text = input()

    if text == 'STOP' and cake_pieces > 0:
        print(f'{cake_pieces} pieces are left.')
        break

    pieces = int(text)
    cake_pieces -= pieces

    if cake_pieces <= 0:
        print(f'No more cake left! You need {abs(cake_pieces)} pieces more.')
        break
