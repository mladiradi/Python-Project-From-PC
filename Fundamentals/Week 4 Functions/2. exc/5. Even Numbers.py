# --- my decision 1 ---
# --- filter()---
def even_num(num):
    return num % 2 == 0


seq = input().split()
seq_in_num_lst = []
for i in seq:
    seq_in_num_lst.append(int(i))
print(list(filter(even_num, seq_in_num_lst)))


# --- my decision 2---
def even_numbers(sequence):
    even_lst = []
    for ii in sequence:
        if int(ii) % 2 == 0:
            even_lst.append(int(ii))
    return even_lst


sequence_lst = input().split()
result = even_numbers(sequence_lst)
print(result)


# --- lambda ---
numbers_as_string = input().split()
numbers_as_digits = []
for number in numbers_as_string:
    numbers_as_digits.append(int(number))
is_even = lambda x: x % 2 == 0
final_list = list(filter(is_even, numbers_as_digits))
print(final_list)


# ---list copmrehension---

print([int(number) for number in input().split() if int(number) % 2 == 0])
