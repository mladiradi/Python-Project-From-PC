
key = list(map(int, input().strip().split()))
key_length = len(key)

while True:
    line = input().strip()
    if line == "find":
        break

    decrypted_message = []

    for i, char in enumerate(line):
        key_value = key[i % key_length]
        decrypted_char = chr(ord(char) - key_value)
        decrypted_message.append(decrypted_char)

    decrypted_message = ''.join(decrypted_message)
    type_start = decrypted_message.find('&') + 1
    type_end = decrypted_message.find('&', type_start)
    coordinates_start = decrypted_message.find('<') + 1
    coordinates_end = decrypted_message.find('>', coordinates_start)

    if 0 < type_start < type_end and \
            0 < coordinates_start < coordinates_end:

        treasure_type = decrypted_message[type_start:type_end]
        coordinates = decrypted_message[coordinates_start:coordinates_end]
        print(f"Found {treasure_type} at {coordinates}")
