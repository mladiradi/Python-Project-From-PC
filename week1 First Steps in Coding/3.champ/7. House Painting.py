x = float(input())
y = float(input())
h = float(input())

side_wall = 2 * (x * y) - 2 * (1.5 * 1.5)
front_wall = 2 * (x * x) - 1.2 * 2
green = (side_wall + front_wall) / 3.4

top_roof = 2 * (x * y)
front_roof = 2 * (x * h / 2)
red = (top_roof + front_roof) / 4.3

print('%.2f' % green)
print('%.2f' % red)
