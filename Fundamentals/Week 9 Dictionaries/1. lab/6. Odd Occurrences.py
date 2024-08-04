
data = input().split()

data_dict = {}

for i in data:
    lower_i = i.lower()
    if lower_i not in data_dict:
        data_dict[lower_i] = 1
    else:
        data_dict[lower_i] += 1

for key, value in data_dict.items():
    if value % 2 != 0:
        print(key, end=" ")

# # input:
#
# Java C# PHP PHP JAVA C java

# # result:
#
# java c# c