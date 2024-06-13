
def odd_and_even_counter(number_str):
    odd_sum = 0
    even_sum = 0
    for i in number_str:
        if int(i) % 2 != 0:
            odd_sum += int(i)
        else:
            even_sum += int(i)
    return print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


num = input()
odd_and_even_counter(num)


def odd_even_sums(some_number: str):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for digit in some_number:
        if int(digit) % 2 == 0:
            sum_of_even_digits += int(digit)
        else:
            sum_of_odd_digits += int(digit)
    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"


number = input()
print(odd_even_sums(number))
