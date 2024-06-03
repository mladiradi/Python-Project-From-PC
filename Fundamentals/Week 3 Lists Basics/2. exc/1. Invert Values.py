
# received_strings = input()
#
# lst_of_strings = received_strings.split(" ")
# lst_of_opposite = []
#
# for i in lst_of_strings:
#     number = -int(i)
#     lst_of_opposite.append(number)
# print(lst_of_opposite)

list_with_numbers = input().split()  # дирекно съставя листа, като разделя символите с интервал " "

opposite_numbers = []             # opposite_numbers = list

for number in list_with_numbers:
    opposite_number = -int(number)
    opposite_numbers.append(opposite_number)
print(opposite_numbers)
