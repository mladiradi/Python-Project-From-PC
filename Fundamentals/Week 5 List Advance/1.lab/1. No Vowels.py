def clean_text(letter_text):
    return [index for index in letter_text if index.lower() not in ['a', 'o', 'u', 'e', 'i']]


text = input()
print(''.join(clean_text(text)))


text = input()
index = ''
for i in text:
    # if i.lower() not in ['a', 'o', 'u', 'e', 'i']: # обръща всички символи в малки само за проверката в if-a
    index += i.lower() # превръща големите в малки

print(''.join(index))
