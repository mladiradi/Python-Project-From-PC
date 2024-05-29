
prime = 0
non_prime = 0

while True:
    text = input()

    if text == 'stop':
        print(f'Sum of all prime numbers is: {prime}')
        print(f'Sum of all non prime numbers is: {non_prime}')
        break
    num = int(text)
    if num < 0:
        print('Number is negative.')
        num = 0
    check = True
    for i in range(2, num):

        if num % i == 0:
            check = False
            break
    if check:
        prime += num
    else:
        non_prime += num

# prime = 0
# non_prime = 0
#
# while True:
#     command = input()
#     if command != 'stop':
#         number = int(command)
#         if number > 1:
#             is_prime = True
#             for i in range(2, number):
#                 if number % i == 0:
#                     is_prime = False
#                     break
#             if is_prime:
#                 prime += number
#             else:
#                 non_prime += number
#         elif number < 0:
#             print("Number is negative.")
#     else:
#         break
# 
# print(f'Sum of all prime numbers is: {prime}')
# print(f'Sum of all non prime numbers is: {non_prime}')
