
# budget = int(input())
#
# while True:
#     text = input()
#     if text == 'End':
#         print('You bought everything needed.')
#         break
#     price = int(text)
#     budget -= price
#     if budget < 0:
#         print('You went in overdraft!')
#         break

budget = int(input())
text = input()

while text != "End":
    price = int(text)
    budget -= price

    if budget < 0:
        print('You went in overdraft!')
        break
    text = input()
else:
    print('You bought everything needed.')
