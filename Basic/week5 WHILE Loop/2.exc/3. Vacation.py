# need_money = float(input())
# own_money = float(input())
#
# d_counter = 0
# spend_counter = 0
#
# while own_money < need_money and spend_counter < 5:
#     command = input()
#     money = float(input())
#     d_counter += 1
#
#     if command == 'save':
#         own_money += money
#         spend_counter = 0
#
#     elif command == 'spend':
#         own_money -= money
#         spend_counter += 1
#
#         if own_money < 0:
#             own_money = 0
#
#     if spend_counter == 5:
#         print("You can't save the money.")
#         print(d_counter)
#         break
#
#     if own_money >= need_money:
#         print(f'You saved the money for {d_counter} days.')
#         break

need_money = float(input())
cash_money = float(input())

counter = 0
spend_counter = 0

while True:
    action = input()
    action_money = float(input())
    counter += 1

    if action == 'save':
        cash_money += action_money
        spend_counter = 0

    if action == 'spend':
        cash_money -= action_money
        spend_counter += 1

        if cash_money < 0:
            cash_money = 0

    if spend_counter == 5:
        print("You can't save the money.")
        print(counter)
        break

    if cash_money >= need_money:
        print(f'You saved the money for {counter} days.')
        break
