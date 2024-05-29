
num = int(input())

for n in range(1, num + 1):
    sum_of_digit = 0
    digits = n

    while digits > 0:
        sum_of_digit += digits % 10
        digits = int(digits / 10)

    if (sum_of_digit == 5) or (sum_of_digit == 7) or (sum_of_digit == 11):
        print(f'{n} -> True')
    else:
        print(f'{n} -> False')
