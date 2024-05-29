
symbol = ""
final = ""
word = ""

cn = 0
co = 0
cc = 0

while True:

    symbol = input()
    if chr(65) <= symbol <= chr(90) or chr(97) <= symbol <= chr(122):

        if symbol == "End":
            break

        if symbol == 'n' and cn == 0:
            cn += 1

        elif symbol == 'o' and co == 0:
            co += 1

        elif symbol == 'c' and cc == 0:
            cc += 1

        else:
            word += symbol

        if cn == 1 and co == 1 and cc == 1:
            word += " "
            final = word

            cn = 0
            co = 0
            cc = 0
    else:
        continue

print(final)
