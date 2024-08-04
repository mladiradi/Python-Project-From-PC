
char_list = input().split(", ")
dict_list = {}

for i in char_list:
    dict_list[i] = ord(i)

print(dict_list)


char_dict = {char: ord(char) for char in input().split(', ')}
print(char_dict)

# # input:
# a, b, c, a

# # result:
# {'a': 97, 'b': 98, 'c': 99}
