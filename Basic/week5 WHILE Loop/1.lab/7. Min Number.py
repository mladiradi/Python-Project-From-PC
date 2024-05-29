import sys

min_num = sys.maxsize

while True:
    text = str.lower(input())

    if text == 'stop':
        print(min_num)
        break

    num_input = int(text)

    if num_input < min_num:
        min_num = num_input
