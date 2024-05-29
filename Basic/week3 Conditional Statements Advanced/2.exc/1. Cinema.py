type_m = str.lower(input())
row = int(input())
column = int(input())

profit = 0
seat = row * column

if type_m == 'premiere':
    profit = 12
elif type_m == 'normal':
    profit = 7.5
elif type_m == 'discount':
    profit = 5
print(f'{seat * profit:.2f} leva')
