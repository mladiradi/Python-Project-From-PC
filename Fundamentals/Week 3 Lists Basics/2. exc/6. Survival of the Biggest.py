
lst_of_integers = input().split()
count_of_numbers = int(input())

lst_of_numbers = []

for numbers in lst_of_integers:
    lst_of_numbers.append(int(numbers))

for i in range(count_of_numbers):
    min_number = min(lst_of_numbers)
    lst_of_numbers.remove(min_number)

for i in range(len(lst_of_numbers) - 1):
    print(lst_of_numbers[i], end=", ")
print(lst_of_numbers[-1])

# i = 0
# while i < len(lst_of_numbers):                    # print with while
#     if i < (len(lst_of_numbers) - 1):
#         print(lst_of_numbers[i], end=", ")
#         i += 1
#     else:
#         print(lst_of_numbers[i])
#         break

# for i in range(len(lst_of_numbers)):              # print with for
#     if i < (len(lst_of_numbers) - 1):
#         print(lst_of_numbers[i], end=", ")
#     else:
#         print(lst_of_numbers[i])
