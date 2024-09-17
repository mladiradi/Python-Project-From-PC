
# https://pastebin.com/b4B2xm49

import re

text = input()

while text:

    pattern = r'\d+'
    matches = re.findall(pattern, text)
    if matches:
        print(' '.join(matches), end=" ")
    text = input()

# # input:
#
# The300
# What is that?
# I think it's the 3rd movie
# Let's watch it at 22:45

# # result:
#
# 300 3 22 45
