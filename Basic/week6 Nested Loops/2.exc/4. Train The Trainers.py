
juri = int(input())

name = ''
sum_scores = 0
total_scores = 0
counter = 0

while True:
    text = input()
    if text == 'Finish':
        print(f"Student's final assessment is {total_scores / counter:.2f}.")
        break
    else:
        name = text

    for i in range(juri):
        num = float(input())
        sum_scores += num
        counter += 1
    print(f"{name} - {sum_scores / juri:.2f}.")

    total_scores += sum_scores
    sum_scores = 0


# juri = int(input())
# total_number = 0
# total_scores = 0
#
# while True:
#     command = input()
#     if command == 'Finish':
#         print(f"Student's final assessment is {total_scores / total_number:.2f}.")
#         break
#     else:
#         presentation = ''
#         presentation = command
#         sum_score = 0
#
#         for i in range(juri):
#             score = float(input())
#             sum_score += score
#             total_scores += score
#             total_number += 1
#
#         print(f"{presentation} - {sum_score / juri:.2f}.")
