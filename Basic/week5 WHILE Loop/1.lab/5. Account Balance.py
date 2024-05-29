# start = input()
# sum_money = 0.0
#
# while start != 'NoMoreMoney':
#     money = float(start)
#
#     if money <= 0:
#         print('Invalid operation!')
#         break
#
#     sum_money += money
#     print(f'Increase: {money:.2f}')
#     start = input()
#
# print(f'Total: {sum_money:.2f}')


sum_money = 0

while True:
    text = input()

    if text == 'NoMoreMoney':
        break
    money = float(text)

    if money >= 0:
        sum_money += money
        print(f'Increase: {money:.2f}')
    else:
        print('Invalid operation!')
        break

print(f'Total: {sum_money:.2f}')
