
str = input()
n = 0

for char in str:
    if char == 'a':
        n += 1
    elif char == 'e':
        n += 2
    elif char == 'i':
        n += 3
    elif char == 'o':
        n += 4
    elif char == 'u':
        n += 5

print(n)
