
number = int(input())

if number <= 1:
    print('False')
elif number <= 3:
    print('True')
elif number % 2 == 0 or number % 3 == 0:
    print('False')
else:
    print('True')

# num = int(input())
# if num > 1:
#     for i in range(2, (num // 2) + 1):
#         if num % i == 0:
#             print("False")
#             break
#     else:
#         print("True")
# else:
#     print("False")
