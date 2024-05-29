import math

num = int(input())

red_n = 0
ora_n = 0
yel_n = 0
whi_n = 0
bla_n = 0
points = 0
other_col = 0

for i in range(num):
    text = input()
    if text == 'red':
        points += 5
        red_n += 1
    elif text == 'orange':
        points += 10
        ora_n += 1
    elif text == 'yellow':
        points += 15
        yel_n += 1
    elif text == 'white':
        points += 20
        whi_n += 1
    elif text == 'black':
        points = math.floor(points / 2)
        bla_n += 1
    else:
        other_col += 1

print(f'Total points: {points}')
print(f'Red balls: {red_n}')
print(f'Orange balls: {ora_n}')
print(f'Yellow balls: {yel_n}')
print(f'White balls: {whi_n}')
print(f'Other colors picked: {other_col}')
print(f'Divides from black balls: {bla_n}')
