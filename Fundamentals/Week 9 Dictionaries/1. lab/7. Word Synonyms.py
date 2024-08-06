
cycles = int(input())
syn_dict = {}

for i in range(cycles):
    key = input()
    value = input()

    if key not in syn_dict:
        syn_dict[key] = []
        syn_dict[key].append(value)
    else:
        syn_dict[key].append(value)

for i in syn_dict:
    print(f"{i} - {', '.join(syn_dict[i])}")

# # input:
# 3
# cute
# adorable
# cute
# charming
# smart
# clever

# # result:
# cute - adorable, charming
# smart - clever

# n = int(input())
# synonyms = {}
#
# for i in range(n):
#     word = input()
#     synonym_w = input()
#
#     if word in synonyms:
#         synonyms[word].append(synonym_w)
#     else:
#         synonyms[word] = [synonym_w]
#
# for word, synonym_lst in synonyms.items():
#     synonym_str = ', '.join(synonym_lst)
#     print(f'{word} - {synonym_str}')
