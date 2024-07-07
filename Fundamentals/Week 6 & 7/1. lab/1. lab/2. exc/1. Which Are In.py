
def sub_in_main_strngs(sub, full):
    sub_lst = []

    for curr_sub in sub:
        for curr_full in full:
            if curr_sub in curr_full:
                sub_lst.append(curr_sub)
                break
    return sub_lst


substrngs = input().split(", ")
fullstrngs = input().split(", ")
result = sub_in_main_strngs(substrngs, fullstrngs)
print(result)


def sub_in_main_strngs(sub, full):
    return [curr_sub for curr_sub in sub
            if any(curr_sub in curr_full for curr_full in full)]


substrngs = input().split(", ")
fullstrngs = input().split(", ")
result = sub_in_main_strngs(substrngs, fullstrngs)
print(result)
