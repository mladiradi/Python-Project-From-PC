
n = int(input())
word = input()
strings = []

for i in range(n):
    current_string = input()
    strings.append(current_string)
print(strings)

for i in range(len(strings) - 1, -1, -1):
    if word not in strings[i]:
        strings.remove(strings[i])

print(strings)


#  моя начин чрез добавяне, а не като горния с изваждане на несъвпадението
# n = int(input())
# word_given = input()
#
# text_list = []
# given_list = []
#
# for i in range(n):
#     text = input()
#     text_list.append(text)
#
# for i in range(len(text_list)):
#     row = text_list[i]
#     if word_given in row:
#         given_list.append(row)
#
# print(text_list)
# print(given_list)
