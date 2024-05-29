
name = input()
packet = input()
ticket_num = int(input())

price = 0

if name == 'John Wick':
    if packet == 'Drink':
        price = 12
    elif packet == 'Popcorn':
        price = 15
    elif packet == 'Menu':
        price = 19

elif name == 'Star Wars':
    if packet == 'Drink':
        price = 18
    elif packet == 'Popcorn':
        price = 25
    elif packet == 'Menu':
        price = 30

elif name == 'Jumanji':
    if packet == 'Drink':
        price = 9
    elif packet == 'Popcorn':
        price = 11
    elif packet == 'Menu':
        price = 14

if name == 'Star Wars' and ticket_num >= 4:
    price *= 0.7
elif name == 'Jumanji' and ticket_num == 2:
    price *= 0.85

total = ticket_num * price

print(f"Your bill is {total:.2f} leva.")
