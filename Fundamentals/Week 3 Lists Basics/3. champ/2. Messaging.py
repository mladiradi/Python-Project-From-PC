
numbers = input().split()
message = input()

lst_of_message = []
num_letter = 0

for num in numbers:
    sum_i = 0
    for i in num:
        sum_i += int(i)

    index = sum_i % len(message)

    lst_of_message.append(message[index])
    message = message.replace(message[index], "", 1)

print(''.join(lst_of_message))

# numbers_list = input().split(' ')
# init_message = input()
# message_list = []
#
# for sequence in numbers_list:
#     current_sum = 0
#     for i in sequence:
#         current_sum += int(i)
#
#     current_sum %= len(init_message)
#
#     message_list.append(init_message[current_sum])
#     init_message = init_message.replace(init_message[current_sum], '', 1)
#
# print(''.join(message_list))
