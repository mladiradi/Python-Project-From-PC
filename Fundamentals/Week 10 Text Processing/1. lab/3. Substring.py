
word = input()
letters = input()

while word in letters:
    letters = letters.replace(word, "")

print(letters)

# # input:
#
# ice
# kicegiciceeb

# # result:
#
# kgb