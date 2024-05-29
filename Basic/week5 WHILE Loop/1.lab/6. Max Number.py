import sys

max_num = -sys.maxsize

while True:
    text = str.lower(input())

    if text == 'stop':
        print(max_num)
        break

    num_input = int(text)

    if num_input > max_num:
        max_num = num_input
