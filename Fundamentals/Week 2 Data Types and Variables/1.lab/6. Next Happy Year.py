
year = int(input()) + 1  # започва проверката от следващата година +1

while len(set(str(year))) != len(str(year)):
    year += 1

print(year)

