
fruits = input().split()
result = [word for word in fruits if len(word) % 2 == 0]
print('\n'.join(result))
