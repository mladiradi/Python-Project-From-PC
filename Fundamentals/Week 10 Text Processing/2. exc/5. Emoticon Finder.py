
text = input()

for i in range(len(text)):
    if text[i] == ":":
        symbol = text[i + 1]
        print(f":{symbol}")


# # input:
#
# There are so many emoticons nowadays :P. I have many ideas :O what input to place here :)


# # result:
#
# :P
# :O
# :)

single_string = input()
for index in range(len(single_string)):
    if single_string[index] == ':':
        print(f":{single_string[index+1]}")
