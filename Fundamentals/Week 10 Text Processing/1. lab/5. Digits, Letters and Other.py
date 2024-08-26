
text = input()
digits = ""
letters = ""
other = ""

for i in text:
    if i.isdigit():
        digits += i
    elif i.isalpha():
        letters += i
    else:
        other += i

print(digits)
print(letters)
print(other)

# # input:
#
# Agd#53Dfg^&4F53

# # result:
#
# 53453
# AgdDfgF
# #^&
