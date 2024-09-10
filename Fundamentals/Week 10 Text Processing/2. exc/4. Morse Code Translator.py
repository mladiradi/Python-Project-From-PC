
morse_to_text = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z'
}

input_data = []
while True:
    try:
        line = input().strip()
        if line:
            input_data.append(line)
        else:
            break
    except EOFError:
        break

input_string = ' '.join(input_data)

translated_words = []
for morse_word in input_string.split(' | '):
    translated_letters = [morse_to_text[letter] for letter in morse_word.split()]
    translated_words.append(''.join(translated_letters))

print(' '.join(translated_words))

import sys

morse_to_text = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z'
}

input_string = sys.stdin.read().strip()

translated_words = []
for morse_word in input_string.split(' | '):
    translated_letters = [morse_to_text[letter] for letter in morse_word.split()]
    translated_words.append(''.join(translated_letters))

print(' '.join(translated_words))
