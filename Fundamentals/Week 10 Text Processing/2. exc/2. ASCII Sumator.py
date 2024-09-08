start_char = input().strip()
end_char = input().strip()

random_string = input().strip()

start_ascii = ord(start_char)
end_ascii = ord(end_char)

if start_ascii > end_ascii:
    start_ascii, end_ascii = end_ascii, start_ascii

ascii_sum = 0

for char in random_string:
    char_ascii = ord(char)
    if start_ascii < char_ascii < end_ascii:
        ascii_sum += char_ascii

print(ascii_sum)
