
def rounding_list(list_numbers) -> list:
    rounded_lst = []
    for i in list_numbers:
        rounded_lst.append(round(float(i)))
    return rounded_lst


float_list = input().split()  # expecting given numbers, separated by a single space
result = rounding_list(float_list)
print(result)
