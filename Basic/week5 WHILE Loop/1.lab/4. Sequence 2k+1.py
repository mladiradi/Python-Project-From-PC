first_num = int(input())

counter = 1

while True:
    print(counter)
    counter = 2 * counter + 1

    if counter > first_num:
        break
