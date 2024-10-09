
password = input()

while True:
    text = input()
    if text == "Done":
        break

    command = text.split()
    action = command[0]

    if action == "TakeOdd":
        new_password = password
        password = ""
        for i in range(len(new_password)):
            if i % 2 != 0:
                password += new_password[i]
        print(password)

    elif action == "Cut":
        index, length = int(command[1]), int(command[2])
        password = password[:index] + password[index + length:]
        print(password)

    elif action == "Substitute":
        substring, substitute = command[1], command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

print(f"Your password is: {password}")

# # input:
#
# Siiceercaroetavm!:?:ahsott.:i:nstupmomceqr
# TakeOdd
# Cut 15 3
# Substitute :: -
# Substitute | ^
# Done
#
# # 2:
#
# up8rgoyg3r1atmlmpiunagt!-irs7!1fgulnnnqy
# TakeOdd
# Cut 18 2
# Substitute ! ***
# Substitute ? .!.
# Done
#
#
# # output:
#
# icecream::hot::summer
# icecream::hot::mer
# icecream-hot-mer
# Nothing to replace!
# Your password is: icecream-hot-mer
#
# # 2:
#
# programming!is!funny
# programming!is!fun
# programming***is***fun
# Nothing to replace!
# Your password is: programming***is***fun
