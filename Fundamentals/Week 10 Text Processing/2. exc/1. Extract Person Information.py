import re

n = int(input().strip())

name_pattern = r'@([^|]+)\|'
age_pattern = r'#(\d+)\*'

for _ in range(n):
    line = input().strip()

    names = re.findall(name_pattern, line)
    ages = re.findall(age_pattern, line)

    for name, age in zip(names, ages):
        print(f"{name} is {age} years old.")
