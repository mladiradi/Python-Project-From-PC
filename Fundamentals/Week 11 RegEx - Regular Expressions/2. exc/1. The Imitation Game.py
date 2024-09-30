
crypted_mess = input()

while True:
    text = input()
    if text == "Decode":
        break

    parts = text.split("|")
    operation = parts[0]
    if operation == "Move":
        number_of_letters = int(parts[1])
        left_side = crypted_mess[:number_of_letters]
        right_side = crypted_mess[number_of_letters:]
        crypted_mess = right_side + left_side
        # print(moved_message)
    elif operation == "Insert":
        given_index = int(parts[1])
        value = parts[2]
        left_side = crypted_mess[:given_index]
        right_side = crypted_mess[given_index:]
        crypted_mess = left_side + value + right_side
        # print(inserted_value)
    elif operation == "ChangeAll":
        substring = parts[1]
        replacement = parts[2]
        crypted_mess = crypted_mess.replace(substring, replacement)

print(f"The decrypted message is: {crypted_mess}")

# # input:
#
# zzHe
# ChangeAll|z|l
# Insert|2|o
# Move|3
# Decode


# # output:
#
# The decrypted message is: Hello
