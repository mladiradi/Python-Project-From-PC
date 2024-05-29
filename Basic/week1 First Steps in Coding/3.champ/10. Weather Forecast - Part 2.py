deg = float(input())

if 5 <= deg < 12:
    print('Cold')
elif 12 <= deg < 15:
    print('Cool')
elif 15 <= deg <= 20:
    print('Mild')
elif 20 < deg < 26:
    print('Warm')
elif 26 <= deg < 35:
    print('Hot')
else:
    print('unknown')

# deg = float(input())
#
# if deg < 5:
#     print('unknown')
# elif deg < 12:
#     print('Cold')
# elif deg < 15:
#     print('Cool')
# elif deg <= 20:
#     print('Mild')
# elif deg < 26:
#     print('Warm')
# elif deg <= 35:
#     print('Hot')
# else:
#     print('unknown')