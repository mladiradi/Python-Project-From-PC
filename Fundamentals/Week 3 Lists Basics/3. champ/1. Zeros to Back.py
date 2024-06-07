
num = input().split(", ")
lst_int_num = []
lst_zero = []

for i in num:
    if i == "0":
        lst_zero.append(int(i))
    else:
        lst_int_num.append(int(i))

for i in lst_zero:
    lst_int_num.append(i)

print(lst_int_num)
