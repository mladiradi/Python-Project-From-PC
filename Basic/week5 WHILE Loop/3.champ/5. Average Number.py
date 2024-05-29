
begin = int(input())

counter = 0
sum_number = 0

while True:
    number = float(input())

    sum_number += number
    counter += 1

    if counter == begin:
        print(f'{sum_number / counter:.2f}')
        break
