
import re

names = input()
regex = "\\b[A-Z][a-z]+ [A-Z][a-z]+\\b"
# regex = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b' # 2 вариант
matches = re.findall(regex, names)
print(" ".join(matches))
# print(matches) # 2 вариант

# # input:
#
# Peter Smith, peter smith, Peter smith, peter Smith, PEter Smith, Peter SmIth, Lily Everett

# # output:
#
# Peter Smith Lily Everett
