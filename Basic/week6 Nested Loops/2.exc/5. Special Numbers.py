
num = int(input())

for i in range(1111, 9999):
    num_str = str(i)
    total = 0
    for ii in num_str:
        if int(ii) != 0:
            if num % int(ii) == 0:
                total += 1
            if total == 4:
                print(i, end=' ')
