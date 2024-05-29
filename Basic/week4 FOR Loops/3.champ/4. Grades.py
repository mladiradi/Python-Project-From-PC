students_num = int(input())

score_2_count = 0
score_3_count = 0
score_4_count = 0
score_5_count = 0
sum_score = 0

for i in range(0, students_num):
    score = float(input())
    if score < 3:
        score_2_count += 1
    elif score < 4:
        score_3_count += 1
    elif score < 5:
        score_4_count += 1
    else:
        score_5_count += 1
    sum_score += score

average_score = sum_score / students_num

print(f'Top students: {score_5_count / students_num * 100:.2f}%')
print(f'Between 4.00 and 4.99: {score_4_count / students_num * 100:.2f}%')
print(f'Between 3.00 and 3.99: {score_3_count / students_num * 100:.2f}%')
print(f'Fail: {score_2_count / students_num * 100:.2f}%')
print(f'Average: {average_score:.2f}')
