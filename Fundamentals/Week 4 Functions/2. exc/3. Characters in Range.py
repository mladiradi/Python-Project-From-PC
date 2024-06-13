
def characters_in_range(a, b) -> chr:
    num_a = ord(a)
    num_b = ord(b)
    lst_of_chars = []
    for i in range(num_a + 1, num_b):
        lst_of_chars.append(chr(i))
    return lst_of_chars


char_a = input()
char_b = input()
print(" ".join(characters_in_range(char_a, char_b)))


def all_the_characters(first_char, second_char):
    characters = []
    for current_character_as_digit in range(ord(first_char) + 1, ord(second_char)):
        characters.append(chr(current_character_as_digit))
    return characters


first_character = input()
second_character = input()
result = all_the_characters(first_character, second_character)
print(" ".join(result))
