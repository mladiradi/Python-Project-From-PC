
multiplier_num = int(input())
counter_num = int(input())

lst_of_num = []

for i in range(1, counter_num + 1):
    number = i * multiplier_num
    lst_of_num.append(number)
    # lst_of_num.append(i * multiplier_num)
print(lst_of_num)
