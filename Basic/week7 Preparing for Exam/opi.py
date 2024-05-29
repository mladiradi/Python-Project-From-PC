
counter = 0
length_text = 0
sum_length_text = 0
word = 0
max_length = 0
name = ''

while True:
    text = input()

    if text == 'STOP':
        break

    for char in text:
        word += 1

    for char in text:
        if chr(65) <= char <= chr(90):
            length_text = ord(char) - word
        elif chr(97) <= char <= chr(122):
            length_text = ord(char) - (word * 2)
        else:
            length_text = ord(char)

        sum_length_text += length_text

    if sum_length_text > max_length:
        max_length = sum_length_text
        name = text

    sum_length_text = 0
    word = 0
    counter += 1

    if counter == 7:
        print("The limit is reached.")
        break

print(f"The best movie for you is {name} with {max_length} ASCII sum.")
