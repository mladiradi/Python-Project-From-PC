# от решение на студент
# numbers = input()
# beggars = int(input())
#
# numbers = list(map(int, numbers.split(", ")))
# result = [0] * beggars
# for i in range(len(numbers)):
#     result[i % beggars] += numbers[i]
# print(result)

string_of_money = input().split(", ")
num_of_beggars = int(input())

lst_of_int_money = []
lst_total_money = []
start_i = 0

for money in string_of_money:
    lst_of_int_money.append(int(money))

for beggars in range(num_of_beggars):
    sum_money = 0
    for i in range(start_i, len(lst_of_int_money), num_of_beggars):
        sum_money += lst_of_int_money[i]
    lst_total_money.append(sum_money)
    start_i += 1
print(lst_total_money)
