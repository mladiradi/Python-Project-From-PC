
keys = ['name', 'age', 'major']
values = ['John', '35', 'Developer']

student = {}

for i in range(len(keys)):
    key = keys[i]
    value = values[i]
    student[key] = value

    print(student[key])
print(student)
print()
# -------------------------------------------------------

students = dict(name='John', age='35', major='Developer')
print(students)

# --------------------------------------------------------

keys = ['name', 'age', 'major']
values = ['John', '35', 'Developer']

student = dict(zip(keys, values))
print(student)

# ----------------------------------------------------------

student = {'name': 'John', 'age': '35', 'major': 'Developer'}

print(student['name'])
print(student['age'])
print(student['major'])

# -----------------------------------------------------------

my_dict = {
 'fruit': 'apple',
 'vegetable': 'cucumber',
 'diary': 'milk',
}

print(my_dict)

# ----------------------------------------------------

my_dict = {'name': 'Jack', 'age': 26}
print(my_dict['name'])  # Jack
print(my_dict.get('age'))  # 26
# my_dict['address']  # KeyError
my_dict.get('address')  # None

# ----------------------------------------------------

my_dicts = {'name': 'Jack', 'age': 26}
my_dicts['age'] = 27  # update
print(my_dicts['age'])  # 27

# ----------------------------------------------------

# keys methods

squares = {1: 1, 2: 4, 3: 9}
for key in squares.keys():
    print(key, end=" ")  # 1 2 3

# ----------------------------------------------------
print()
squares = {1: 1, 2: 4, 3: 9}
for key in squares.keys():
    squares[key] *= 2  # {1: 2, 2: 8, 3: 18}

print(squares)

# ------------------------------------------------------

squares = {1: 1, 2: 4, 3: 9}

for key in squares.keys():
    print(key, squares[key])
print()

for value in squares.values():
    print(value)

# -----------------------------------------------------

squares = {
 1: 1,
 2: 4,
 3: 9,
}
for (key, value) in squares.items():  # item = 1:1, следващия е 2:4
    print(f"Key: {key}, Value: {value}")

# -------------------------------------------------------

my_dict = {'name': 'Peter', 'age': 22}
if 'name' in my_dict.keys():  # You can skip keys()
    print(my_dict['name'])  # Peter

my_dict = {'name': 'Peter', 'age': 22}
if 22 in my_dict.values():
    print("22 is a value in the dictionary")
# 22 is a value in the dictionary

# ------------------------------------------------------
# clear method - remove elements from dict
my_dict = {1: 'apple', 2: 'banana'}
my_dict.clear()
print(my_dict)  # {}

# copy() - returns a copy of dictionary
my_dict = {1: 'apple', 2: 'banana'}
copied_dict = my_dict.copy()
print(my_dict == copied_dict)  # True

# pop() - removes and returns an item from a dictionary having the
# given key
my_dict = {"fruit": "apple", "vegetable": "cucumber"}
apple = my_dict.pop("fruit")  # 'apple'
print(my_dict)  # {'vegetable': 'cucumber'}

# popitem() - removes an item that was last inserted and returns it
# as a tuple - (key, value)
my_dict = {"fruit": "apple", "vegetable": "cucumber"}
print(my_dict.popitem())  # ("vegetable", "cucumber")
print(my_dict)  # {"fruit": "apple"}

# del keyword - removes an item with a specified key name
students = {"name": "George", "course": "Fundamentals"}
del students["course"]
print(students)  # {"name": "George"}

# del keyword can also delete the dictionary completely
students = {"name": "George", "course": "Fundamentals"}
del students
# print(students)  # NameError

# ----------------------------------------------
# nested dictionary

# creating  a nested dictionary
students = {1: {'name': 'Peter', 'age': 22},
            2: {'name': 'Alex', 'age': 21}}
for key, value in students.items():
    print(key, value)
print()
for value in students.values():
    print(value)
print()
for value in students.values():
    for key, curr_value in value.items():
        print(key, curr_value)
print()
# accessing an element
first_student_name = students[1]['name']
print(first_student_name)  # Peter

# adding an element
students[3] = {}  # {3: {}}
students[3]['name'] = 'Amy'  # {3: {'name': 'Amy'}}
students[3]['age'] = 25  # {3: {'name': 'Amy', 'age': 25}}

# nested for-loop - using items()method
shopping_list = {
 "foods": {"nuts": "almonds"},
 "drinks": {"soft": "lemonade", "wine": "merlot"}
}
for key, value in shopping_list.items():
    for nested_key, nested_value in value.items():
        print(f'{nested_value} bought')
        shopping_list[key][nested_key] = 'bought'

# ------------------------------------------------------------

# Dictionary Comprehensions

# Creating a dictionary using dictionary comprehension
data = [("Peter", 22), ("Amy", 18), ("George", 35)]
dictionary = {key: value for (key, value) in data}
print(dictionary)
# {'Peter': 22, 'Amy': 18, 'George': 35}

# Form a dictionary with cube values of numbers
nums = [1, 2, 3]
fruits = ['banana', 'kiwi', 'orange']
cubes = {num: num ** 3 for num in nums}
fruits_n = {fruit: len(fruit) for fruit in fruits}
print(cubes)
print(fruits_n)
# {1: 1, 2: 8, 3: 27}
# {'banana': 6, 'kiwi': 4, 'orange': 6}
