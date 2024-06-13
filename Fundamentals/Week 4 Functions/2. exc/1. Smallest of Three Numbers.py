
def at_least_three_num(a, b, c) -> int:
    return min(a, b, c)


num1 = int(input())
num2 = int(input())
num3 = int(input())
result = at_least_three_num(num1, num2, num3)
print(result)


def smallest(some_list: list) -> int:
    return min(some_list)


first_number = int(input())
second_number = int(input())
third_number = int(input())
smallest_number = smallest([first_number, second_number, third_number])
print(smallest_number)
