days = int(input()) - 1
room = input()
rate = input()

price = 0.0

if room == 'apartment':
    if days < 10:
        price = (days * 25.00) * 0.7
    elif 10 <= days <= 15:
        price = (days * 25.00) * 0.65
    else:
        price = (days * 25.00) * 0.5
elif room == 'president apartment':
    if days < 10:
        price = (days * 35.00) * 0.1
    elif 10 <= days <= 15:
        price = (days * 35.00) * 0.85
    else:
        price = (days * 35.00) * 0.8
elif room == 'room for one person':
    price = days * 18.00

if rate == 'positive':
    price += price * 0.25
else:
    price -= price * 0.1

print(f'{price:.2f}')
