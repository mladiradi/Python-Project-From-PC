
while True:
    destination = input()
    if destination == "End":
        break
    need_money = float(input())
    while True:
        money = float(input())
        need_money -= money
        if need_money <= 0:
            print(f'Going to {destination}!')
            break

#
# saved_money = 0
#
# while True:
#     destination = input()
#     if destination == "End":
#         break
#     need_money = float(input())
#     while True:
#         money = float(input())
#         saved_money += money
#         if saved_money >= need_money:
#             print(f'Going to {destination}!')
#             saved_money = 0
#             break
