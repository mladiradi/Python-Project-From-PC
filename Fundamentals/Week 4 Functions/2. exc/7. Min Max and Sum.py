
def min_max_sum_func(raw_lst):
    num_lst = []
    for i in raw_lst:
        num_lst.append(int(i))
    max_num = max(num_lst)
    min_num = min(num_lst)
    sum_nums = sum(num_lst)
    return print(f"The minimum number is {min_num}\n"
                 f"The maximum number is {max_num}\n"
                 f"The sum number is: {sum_nums}")


sequences_lst = input().split()
min_max_sum_func(sequences_lst)
