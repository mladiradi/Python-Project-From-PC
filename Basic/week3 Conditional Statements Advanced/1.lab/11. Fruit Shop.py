prod = str.lower(input())
day = str.lower(input())
quan = float(input())

price = 0

if day == 'saturday' or day == 'sunday':
    if prod == 'banana':
        price = 2.7
    elif prod == 'apple':
        price = 1.25
    elif prod == 'orange':
        price = 0.9
    elif prod == 'grapefruit':
        price = 1.6
    elif prod == 'kiwi':
        price = 3
    elif prod == 'pineapple':
        price = 5.6
    elif prod == 'grapes':
        price = 4.2
    else:
        print('error')
        exit()
elif day == 'monday' or day == 'tuesday' or \
     day == 'wednesday' or day == 'thursday' or \
     day == 'friday':
    if prod == 'banana':
        price = 2.5
    elif prod == 'apple':
        price = 1.2
    elif prod == 'orange':
        price = 0.85
    elif prod == 'grapefruit':
        price = 1.45
    elif prod == 'kiwi':
        price = 2.7
    elif prod == 'pineapple':
        price = 5.5
    elif prod == 'grapes':
        price = 3.85
    else:
        print('error')
        exit()
else:
    print('error')
    exit()

print(f'{price * quan:.2f}')
