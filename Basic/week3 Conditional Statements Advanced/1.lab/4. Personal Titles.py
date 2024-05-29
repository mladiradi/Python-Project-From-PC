age = float(input())
gend = input()

if gend == 'm':
    if age >= 16:
        print('Mr.')
    else:
        print('Master')
elif gend == 'f':
    if age >= 16:
        print('Ms.')
    else:
        print('Miss')
