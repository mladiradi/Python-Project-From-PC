
while True:
    text = input()
    if text == "end":
        break
    text_reverse = ""
    for letter in reversed(text):
        text_reverse += letter
    print(text + " = " + text_reverse)

# # input:
#
# helLo
# Softuni
# bottle
# end

# # result:
#
# helLo = oLleh
# Softuni = inutfoS
# bottle = elttob
