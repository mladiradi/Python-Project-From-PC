
def perfect_number(num):
    sum_of_perfect = 0
    for div in range(1, num):
        if num % div == 0:
            sum_of_perfect += div
    if num == sum_of_perfect:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(perfect_number(number))
