
data = input().split()
bakery = {}

for i in range(0, len(data), 2):
    key = data[i]
    value = data[i + 1]
    bakery[key] = int(value)

print(bakery)

# bread 10 butter 4 sugar 9 jam 12
# result = {'bread': 10, 'butter': 4, 'sugar': 9, 'jam': 12}
