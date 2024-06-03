
n = int(input())

all_numbers = []
filtered_num = []

for i in range(n):
    number = int(input())
    all_numbers.append(number)

text = input()
if text == 'even':
    for i in all_numbers:
        if i % 2 == 0:
            filtered_num.append(i)
elif text == 'odd':
    for i in all_numbers:
        if i % 2!= 0:
            filtered_num.append(i)
elif text == 'negative':
    for i in all_numbers:
        if i < 0:
            filtered_num.append(i)
elif text == 'positive':
    for i in all_numbers:
        if i >= 0:
            filtered_num.append(i)

print(filtered_num)



# Advance

n = int(input())
c_even = 'even'
c_odd = 'odd'
c_negative = 'negative'
c_positive = 'positive'

numbers =[int(input()) for i in range(n)]
filtered_num = []
text = input()

for i in numbers:
    c_filtered = (
        (text == c_even and i % 2 == 0) or
        (text == c_odd and i % 2 != 0) or
        (text == c_positive and i >= 0) or
        (text == c_negative and i < 0)
    )
    if c_filtered:
        filtered_num.append(i)

print(filtered_num)