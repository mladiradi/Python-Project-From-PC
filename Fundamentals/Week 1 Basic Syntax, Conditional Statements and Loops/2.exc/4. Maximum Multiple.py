
divisor = int(input())
boundary = int(input())
number = int

for number in range(boundary, divisor - 1, -1):
    if number % divisor == 0:
        break

print(number)

# largest = (boundary // divisor) * divisor

# largest = boundary - ( boundary % divisor)
