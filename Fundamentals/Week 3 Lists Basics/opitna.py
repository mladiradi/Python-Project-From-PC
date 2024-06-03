
# a, b = b, a - swap

text = "Mladen % Vasev % Raev % a%b "
new_text = text.split("%")
print(new_text)
print()

lst = ['a', 'v', 'r', 'w']
print('-'.join(lst))
print()

lst = ['a', '2', 'r', 'p', 'f']
print(lst[0], lst[2])
print(lst[-2])  # отзад -> напред
print()

add_lst = [1, 2, 3, 7]
add_lst.append(8)
add_lst.append(7)
print(lst)
print()

list_of_numbers = [1, 2, 3, 4, 'dog']
list_of_numbers.remove(3)
list_of_numbers.remove(int(1))
print(list_of_numbers)
print(list_of_numbers[2])  # index на 2-ра позиция от списък list_of_numbers
print(list_of_numbers[-3], list_of_numbers[-1])
print()

# Looping Through Lists
my_list = ["dog", "cat", "fish"]
for element in my_list:
    print(element, end=" ")
print()

for index in range(len(my_list)):
    print(my_list[index], end=" ")
print()

i = 0
while i < len(my_list):             #  отпечатване на лист от int
    print(my_list[i], end=" ")
    i += 1
print()

while my_list:
    print(my_list[0], end=" ")
    current_element = my_list[0]
    my_list.remove(current_element)  # remove
print()
print()
#  ------------------------------------------

my_list = [1, 2, 3, 4]       #  searching in list
if 3 in my_list:
    print("The number 3 is in the list")

my_list = [1, 2, 3, 4, 'koko', 5]       #  searching in list
if 'koko' in my_list:
    print("Koko is in the list")

my_list = [1, 2, 3, 4]
if 5 not in my_list:
    print("The number 5 is not in the list")

a = [1, 2, 3]
b = [a, a]
a[0] = 42
b[0][1] = 99
print(b)