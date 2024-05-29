
num = int(input())

count = 0

for i in range(num + 1):
    for ii in range(num + 1):
        for iii in range(num + 1):
            if i + ii + iii == num:
                count += 1
print(count)
