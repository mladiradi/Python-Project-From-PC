
# while True:
#     text = input()
#     new_text = ''
#
#     if text == 'End':
#         break
#     elif text == 'SoftUni':
#         continue
#
#     for string in text:
#         new_text += string * 2
#     print(new_text)

text = input()

while text != 'End':
    if text != 'SoftUni':
        new_text = ''
        for char in text:
            new_text += char * 2
        print(new_text)
    text = input()
