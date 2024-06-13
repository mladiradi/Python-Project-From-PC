
def sum_number(a, b):
    return a + b


def subtract_numbers(res_of_sum_num, c):
    return res_of_sum_num - c


def subtract_the_add(a, b, c) -> int:
    return subtract_numbers(sum_number(a, b), c)


num1 = int(input())
num2 = int(input())
num3 = int(input())
print(subtract_the_add(num1, num2, num3))


def sum_numbers(first, second):
    return first + second


def subtract(result, third):
    return result - third


def add_and_subtract(first, second, third):
    returned_result = sum_numbers(first, second)
    final_result = subtract(returned_result, third)
    return final_result


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))
