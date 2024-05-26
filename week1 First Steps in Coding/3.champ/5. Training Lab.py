from math import floor

w = float(input())
h = float(input())

row = floor(w / 1.2)
desc = floor((h - 1) / 0.7)

workplace = desc * row - 3

print(workplace)
