
def password_validator(login):
    count = 0
    validation = True
    for _ in login:
        count += 1
    if not 6 <= count <= 10:
        print("Password must be between 6 and 10 characters")
        validation = False

    counter = 0
    for str_and_num in login:
        element = ord(str_and_num)
        if not 48 <= element <= 57 and \
           not 65 <= element <= 90 and \
                not 97 <= element <= 122:
            print("Password must consist only of letters and digits")
            validation = False
            break
        if 48 <= element <= 57:
            counter += 1
    if counter <= 1:
        print("Password must have at least 2 digits")
        validation = False

    if validation:
        print("Password is valid")


password_input = input()
password_validator(password_input)
