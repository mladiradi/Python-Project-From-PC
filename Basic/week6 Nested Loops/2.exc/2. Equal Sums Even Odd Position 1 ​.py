#
# first_num = int(input())
# last_num = int(input())
#
# for i in range(first_num, last_num + 1):
#     num_str = str(i)
#     even_sum = 0
#     odd_sum = 0
#     is_even = 1
#
#     for ii in num_str:
#         if is_even % 2 == 0:
#             even_sum += int(ii)
#
#         else:
#             odd_sum += int(ii)
#
#         is_even += 1
#
#     if even_sum == odd_sum:
#         print(i, end=' ')


start = int(input())
end = int(input())

for i in range(start, end + 1):
    switch_number = str(i)
    even_sum = 0
    odd_sum = 0

    for index, ii in enumerate(switch_number):
        if index % 2 == 0:
            even_sum += int(ii)
        else:
            odd_sum += int(ii)

    if even_sum == odd_sum:
        print(i, end=' ')
