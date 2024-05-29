from math import pi

figure = input()

if figure == 'square':
    side1 = float(input())
    exit = side1 * side1
    print(f'%.3f' % exit)
elif figure == 'rectangle':
    side1 = float(input())
    side2 = float(input())
    exit = side1 * side2
    print(f'%.3f' % exit)
elif figure == 'circle':
    side = float(input())
    exit = side * side * pi
    print(f'%.3f' % exit)
elif figure == 'triangle':
    side1 = float(input())
    side2 = float(input())
    exit = side1 * side2 / 2
    print(f'%.3f' % exit)
