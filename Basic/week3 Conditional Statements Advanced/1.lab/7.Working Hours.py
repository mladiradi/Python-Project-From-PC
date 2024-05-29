hour = int(input())
day = str.lower(input())

if 10 <= hour <= 18 and day != 'sunday':
    print('open')
else:
    print('closed')
