
first_index = int(input())
last_index = int(input())

for index in range(first_index, last_index + 1):

    if index == last_index:
        print(chr(last_index))
    else:
        print(chr(index), end=' ')
        