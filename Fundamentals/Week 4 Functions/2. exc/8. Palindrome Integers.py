

def is_palindrome(some_number_as_string):
    for i in some_number_as_string:
        if i == i[::-1]:
            print("True")
        else:
            print("False")


numbers_as_string = input().split(", ")
is_palindrome(numbers_as_string)


# ---master---
def is_palindrome(some_number_as_string):
    return some_number_as_string == some_number_as_string[::-1]


numbers_as_string = input().split(", ")
for number in numbers_as_string:
    print(is_palindrome(number))