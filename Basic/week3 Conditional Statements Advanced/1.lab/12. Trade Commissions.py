city = str.lower(input())
quan = float(input())

perc = 0

if city == 'sofia':
    if quan < 0:
        print('error')
        exit()
    elif quan <= 500:
        perc = 0.05
    elif quan <= 1000:
        perc = 0.07
    elif quan <= 10000:
        perc = 0.08
    else:
        perc = 0.12
elif city == 'varna':
    if quan < 0:
        print('error')
        exit()
    elif quan <= 500:
        perc = 0.045
    elif quan <= 1000:
        perc = 0.075
    elif quan <= 10000:
        perc = 0.1
    else:
        perc = 0.13
elif city == 'plovdiv':
    if quan < 0:
        print('error')
        exit()
    elif quan <= 500:
        perc = 0.055
    elif quan <= 1000:
        perc = 0.08
    elif quan <= 10000:
        perc = 0.12
    else:
        perc = 0.145
else:
    print('error')
    exit()

print(f'{quan * perc:.2f}')
