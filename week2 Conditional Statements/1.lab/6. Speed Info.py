speed_king = float(input())

if 10 >= speed_king:
    print('slow')
elif 10 < speed_king <= 50:
    print('average')
elif 50 < speed_king <= 150:
    print('fast')
elif 150 < speed_king <= 1000:
    print('ultra fast')
else:
    print('extremely fast')
