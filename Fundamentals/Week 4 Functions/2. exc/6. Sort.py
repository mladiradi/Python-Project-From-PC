
def sorted_list(raw_lst):
    turned_to_num_lst = []
    for i in raw_lst:
        turned_to_num_lst.append(int(i))
    return sorted(turned_to_num_lst)


sequence_lst = input().split()
print(sorted_list(sequence_lst))


def sorted_list(raw_lst):
    return sorted(raw_lst)


sequence_lst = input().split()
print(sorted_list(sequence_lst))
