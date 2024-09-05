
text = input()
final_message = ""
sub_string = ""
repetitions = ""

for index in range(len(text)):
    if not text[index].isdigit():
        sub_string += text[index].upper()
    else:
        for next_characters in range(index, len(text)):
            if not text[next_characters].isdigit():
                break
            repetitions += text[next_characters]
        final_message += sub_string * int(repetitions)
        sub_string = ""
        repetitions = ""
print(f"Unique symbols used: {len(set(final_message))}")
print(final_message)

# # input:
#
# aSd2&5s@1

# # result:
#
# Unique symbols used: 5
# ASDASD&&&&&S@


# Judge не го приема, но показва верен изход от примерите

# text = input()
# upper = ""
# sequence = ""
# unique = ""
#
# for i in range(len(text)):
#     if not text[i].isdigit():
#         upper += text[i].upper()
#     else:
#         if int(text[i]) == 0:
#             sequence += upper
#         for ii in range(int(text[i])):
#             sequence += upper
#         upper = ""
#
# for iii in sequence:
#     if iii not in unique:
#         unique += iii
#
# print(f"Unique symbols used: {len(unique)}")
# print(sequence)
