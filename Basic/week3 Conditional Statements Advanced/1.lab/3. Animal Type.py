name = str.lower(input())

spec = ''

if name == 'dog':
    spec = 'mammal'
elif name == 'crocodile' or name == 'tortoise' or name == 'snake':
    spec = 'reptile'
else:
    spec = 'unknown'
print(spec)
