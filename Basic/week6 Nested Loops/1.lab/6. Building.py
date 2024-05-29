
levels = int(input())
rooms = int(input())

types = ''

for i in range(levels, 0, -1):
    for ii in range(rooms):
        if i == levels:
            types = f'L{i}{ii}'
        elif i % 2 == 0:
            types = f'O{i}{ii}'
        else:
            types = f'A{i}{ii}'

        print(types, end=' ')

    print()
