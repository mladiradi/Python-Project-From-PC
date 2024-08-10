contact_i = {}
while True:
    data = input()
    if "-" not in data:
        break

    name, phone = data.split("-")
    contact_i[name] = phone
    if name in contact_i.keys():
        contact_i[name] = phone

search_num = int(data)
for i in range(search_num):
    name = input()
    if name in contact_i.keys():
        print(f"{name} -> {contact_i[name]}")
    else:
        print(f"Contact {name} does not exist.")


# # input:
# Adam-+359888001122
# Ralf-666
# George-5559393
# Silvester-02/987665544
# 4
# Silvester
# silvester
# Rolf
# Ralf

# # result:
#
# Silvester -> 02/987665544
# Contact silvester does not exist.
# Contact Rolf does not exist.
# Ralf -> 666
