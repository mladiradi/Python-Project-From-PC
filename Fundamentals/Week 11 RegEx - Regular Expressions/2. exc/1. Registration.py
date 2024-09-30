
username = input()

while True:
    command = input()
    if command == "Registration":
        break

    command = command.split()
    action = command[0]

    if action == "Letters":
        case_type = command[1]
        if case_type == "Lower":
            username = username.lower()
        elif case_type == "Upper":
            username = username.upper()
        print(username)

    elif action == "Reverse":
        start_index = int(command[1])
        end_index = int(command[2])
        if (0 <= start_index < len(username)) and (0 <= end_index < len(username)) and (start_index <= end_index):
            substrng = username[start_index:end_index + 1]
            reversed_substrng = substrng[::-1]
            print(reversed_substrng)

    elif action == "Substring":
        substring = command[1]
        if substring in username:
            username = username.replace(substring, "")
            print(username)
        else:
            print(f"The username {username} doesn't contain {substring}.")

    elif action == "Replace":
        str_char = command[1]
        username = username.replace(str_char, "-")
        print(username)

    elif action == "IsValid":
        str_char = command[1]
        if str_char in username:
            print("Valid username.")
        else:
            print(f"{str_char} must be contained in your username.")

# # input:
#
# John
# Letters Lower
# Substring SA
# IsValid @
# Registration
#
# # 2
#
# ThisIsSoftUni
# Reverse 1 3
# Replace S
# Substring hi
# Registration


# # output:
#
# john
# The username john doesn't contain SA.
# @ must be contained in your username.

# # 2
# sih
# ThisIs-oftUni
# TsIs-oftUni
