budget = float(input())
categorie = input()
people_num = int(input())

ticket_price = 0

if people_num <= 4:
    budget -= budget * (1 - 0.25)
elif 4 < people_num <= 9:
    budget -= budget * (1 - 0.4)
elif 9 < people_num <= 24:
    budget -= budget * (1 - 0.5)
elif 24 < people_num <= 49:
    budget -= budget * (1 - 0.6)
else:
    budget -= budget * (1 - 0.75)

if categorie == 'VIP':
    ticket_price = 499.99 * people_num
else:
    ticket_price = 249.99 * people_num

wanted_money = abs(budget - ticket_price)

if budget > ticket_price:
    print(f'Yes! You have {wanted_money:.2f} leva left.')
else:
    print(f'Not enough money! You need {wanted_money:.2f} leva.')
