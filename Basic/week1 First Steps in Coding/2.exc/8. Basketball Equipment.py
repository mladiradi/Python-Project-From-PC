tax = int(input())

sneakers = tax * (1 - 0.4)
outfit = sneakers * (1 - 0.2)
ball = outfit * 0.25
access = ball * 0.2

total = tax + sneakers + outfit + ball + access

print(total)
