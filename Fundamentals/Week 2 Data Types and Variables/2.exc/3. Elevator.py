from math import ceil
# import math

num_of_people = int(input())
cap_of_elevator = int(input())

courses = ceil(num_of_people / cap_of_elevator)
# courses = math.ceil(num_of_people / cap_of_elevator)

print(courses)
