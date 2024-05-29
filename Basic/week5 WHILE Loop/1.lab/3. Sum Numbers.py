start_num = int(input())

sum = 0

while True:
    next_num = int(input())
    sum += next_num
    if sum >= start_num:
        print(sum)
        break
