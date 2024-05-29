
num = int(input())

for i in range(num):
    number = int(input())
    # if not number % 2 == 0:
    if number % 2 == 1:
        print(f'{number} is odd!')
        break
else:
    print('All numbers are even.')
