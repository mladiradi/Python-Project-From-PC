#
# def repeat = lambda a, b: a * b -> str:
#     action = text_str * num_int
#     return action
#
#
# text = input()
# n = int(input())
# result = repeat(text, n)
# print(result)


repeat_string = lambda string, num: string * num

inp_str = input()
count_n = int(input())
result = repeat_string(inp_str, count_n)
print(result)
