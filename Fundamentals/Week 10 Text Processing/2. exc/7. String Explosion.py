
text = input()
output = ''
num = 0

for i in range(len(text)):
    if text[i] == ">":
        num += int(text[i + 1])
        output += text[i]
    elif num > 0:
        num -= 1
    elif text[i] != ">":
        output += text[i]

print(output)


# # input:
#
# abv>1>1>2>2asdasd
# pesho>2sis>1a>2akarate>4hexmaster

# # result:
#
# abv>>>>dasd
# pesho>is>a>karate>master

some_string = input()
final_string = ""
strength = 0
for index in range(len(some_string)):
    # Explosion
    if strength > 0 and some_string[index] != ">":
        strength -= 1
    # Explosion mark
    elif some_string[index] == ">":
        final_string += ">"  # some_string[index]
        strength += int(some_string[index+1])
    # No explosion, no explosion mark
    else:
        final_string += some_string[index]
print(final_string)
