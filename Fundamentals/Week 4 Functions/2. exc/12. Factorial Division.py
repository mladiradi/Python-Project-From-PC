
def factorial_division(number):

    for current_number in range(1, number):
        number *= current_number
    return number


num1 = int(input())
num2 = int(input())
factorial_of_num1 = factorial_division(num1)
factorial_of_num2 = factorial_division(num2)
print(f"{factorial_of_num1 / factorial_of_num2:.2f}")
