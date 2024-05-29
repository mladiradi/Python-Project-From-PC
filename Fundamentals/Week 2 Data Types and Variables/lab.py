
value = 'kor'
print(type(value))

# list_example = ['text', 243, 25.5, ['a', 'f'], True, False]

# tuple_examples = ('text', 243, 25.5, ['a', 'f'], True, False)

# set_example = {'text', 243, 25.5, ['a', 'f'], True, False}

# dict_example = {'a': 1, 'f', True, False}

print(isinstance('123', str))
print(isinstance({'a': 1}, dict))


string_examples = 'SoftUni'
print(string_examples[-1]) #от 0 до 6 зашото e 7, -1 за последната буква(отзад напред)
print(len(string_examples))

lst = 'a', 1, True # брой типове данни
print(len(lst))

a1 = 'text'
a2 = "text"
print(a1 == a2)

value = -0 # None,"", 5 , 'a'
print(bool(value))

#set_example
print({1, 1, 1, 1, 1, 2, 3})
print({0, 0, 0, 0})

# year = int(input())
# while len(set(str(year))) != len(str(year)):
#     year += 1
# print(year)

lst = ['az', 'test',2,5]
lst[0] = 'Soft uni'
print(lst)

exmple_dict = {'brand': 'ford', "model": 'Mustang'}
print(exmple_dict['brand'])

for k, v in exmple_dict.items():
    print(k, v)
    print()
    print(k)



