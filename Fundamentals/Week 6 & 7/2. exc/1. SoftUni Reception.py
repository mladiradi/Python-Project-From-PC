# 1 - по-оптимизираната версия
# first_employee_per_hour = int(input())
# second_employee_per_hour = int(input())
# third_employee_per_hour = int(input())
# number_of_students = int(input())
#
# total_efficiency_per_hour = first_employee_per_hour \
#                             + second_employee_per_hour \
#                             + third_employee_per_hour
# total_time = 0
#
# while number_of_students > 0:
#     total_time += 1
#     if total_time % 4 == 0:
#         continue
#     number_of_students -= total_efficiency_per_hour
#
# print(f"Time needed: {total_time}h.")

# 1.1  - инструкторско решение
#
# first_employee_per_hour = int(input())
# second_employee_per_hour = int(input())
# third_employee_per_hour = int(input())
# number_of_students = int(input())
# total_efficiency_per_hour = first_employee_per_hour \
#                             + second_employee_per_hour \
#                             + third_employee_per_hour
# total_time = 0
# hours_counter = 0
# while number_of_students > 0:
#     hours_counter += 1
#     if hours_counter % 4 == 0:
#         total_time += 1
#         continue
#     number_of_students -= total_efficiency_per_hour
#     total_time += 1
# print(f"Time needed: {total_time}h.")

# 1.2
# employee1_efficiency = int(input())
# employee2_efficiency = int(input())
# employee3_efficiency = int(input())
# students_count = int(input())
#
# total_emp_efficiency = employee1_efficiency + employee2_efficiency + employee3_efficiency
#
# total_time = 0
#
# while True:
#     if students_count < 1:
#         total_time = 0
#         break
#     total_time += 1
#     students_count -= total_emp_efficiency
#     if total_time % 4 == 0:
#         total_time += 1
#
#     if students_count <= 0:
#         break
#
# print(f'Time needed: {total_time}h.')
