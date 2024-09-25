import re

text = input()
word = input()

pattern = fr"(?i)\b{word}\b"
matches = re.findall(pattern, text)
print(len(matches))

# # input:
#
# There was one. Therefore I bought it. I wouldn't buy it otherwise.
# there

# # output:
#
# 1