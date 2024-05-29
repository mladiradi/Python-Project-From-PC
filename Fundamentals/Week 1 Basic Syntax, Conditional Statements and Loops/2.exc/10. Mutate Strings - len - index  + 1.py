first = input()
second = input()

for index in range(len(first)):
    left = second[:index + 1]
    right = first[index+1:]
    new = left + right
    if new != first:
        print(new)
        first = new
