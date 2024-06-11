
def calculation(a, b, operator):
    if operator == 'add':
        return a + b
    elif operator == 'divide':
        return int(a / b)
    elif operator == 'multiply':
        return a * b
    return abs(a - b)


operators = input()
first_num = int(input())
second_num = int(input())
result = calculation(first_num, second_num, operators)
print(result)


def calculator(operator, num1, num2):
    return {
        'add': num1 + num2,
        'multiply': num1 * num2,
        'divide': int(num1 / num2),
        'subtract': abs(num1 - num2)
    }.get(operator, 'Invalid operator!')


operator_s = input('Enter the operator: ')
first_num = int(input('Enter first number: '))
second_num = int(input('Enter second number: '))
result = calculator(operator_s, first_num, second_num)
print(result)

