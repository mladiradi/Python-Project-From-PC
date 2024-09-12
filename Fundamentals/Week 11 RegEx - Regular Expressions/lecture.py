
import re

print()


text = """"
I am born on 30-Dec-1995.
My father is born on the 9-Jul-1955.
01-July-2000 is nit valid date.
"""
pattern = r'\b\d{1,2}-[A-Z][a-z]{2}-\d{4}\b'
matches = re.findall(pattern, text)

for match in matches:
    print(match)

# matches = re.finditer(pattern, text)
# for match in matches:
#     print(match)
#     print(match.group())

print()

emails = ['examlpe@amazone.co.uk', 'valid123@email.bg', 'invalid*name@email.bg']
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
for email in emails:
    if re.match(pattern, email):
        print(f'{email} is valid!')
    else:
        print(f'{email} is not valid!')

print()

strng = "The rain in Spain"
x = re.findall("ai", strng)
print(x)
print()

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)
print()

# # Bethany Taylor, Oliver miller, sophia Johnson, SARah Wilson, John Smith, Sam   Smith
# names = input()
# regex = "\\b[A-Z][a-z]+ [A-Z][a-z]+\\b"
# matches = re.findall(regex, names)
# print(" ".join(matches))  # Bethany Taylor John Smith
# print()

strng = "The rain in Spain"
x = re.search("\s", strng)
print("The first white-space character is located in position:", x.start())
print()

strng = "The rain in Spain"
x = re.split("\s", strng)
print(x)
print()

text = 'There are 3 dogs and 4 cats'
result = re.subn('\d', '*****', text)
print(result)
print()

text = 'Apple, aPple and APPLE is a appLE'
pattern = 'apple'
match = re.findall(pattern, text, re.IGNORECASE)
print(match)
