name = input()

counter = 0
counter_min = 0
sum_scores = 0

while True:
    scores = float(input())

    if scores < 4.00:
        counter_min += 1
        if counter_min == 2:
            print(f'{name} has been excluded at {counter + 1} grade')
            break

        continue

    counter += 1
    sum_scores += scores

    if counter == 12:
        print(f'{name} graduated. Average grade: {sum_scores / counter:.2f}')
        break

# name = input()
#
# counter = 0
# counter_min = 0
# sum_scores = 0
#
# while counter < 12:
#     scores = float(input())
#
#     if scores < 4.00:
#         counter_min += 1
#         if counter_min == 2:
#             print(f'{name} has been excluded at {counter + 1} grade')
#             break
#
#         continue
#
#     counter += 1
#     sum_scores += scores
#
# else:
#     print(f'{name} graduated. Average grade: {sum_scores / counter:.2f}')
