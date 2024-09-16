
import re

text = input()
# pattern = "\\b(?P<day>\\d{2})([-.\\/])(?P<month>[A-Z][a-z]{2})\\2(?P<year>\\d{4})\\b"
pattern = r"(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})"  # \2 ще повтори условията в група 2
matches = re.findall(pattern, text)
# matches = re.finditer(pattern, text)

for match in matches:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")

# for match in matches:  # работи с finditer
#     day = match.group(1)
#     month = match.group(3)
#     year = match.group(4)
#     print(f"day: {day}, Month: {month}, Year: {year}")
#


# # input:
#
# 13/Jul/1928, 10-Nov-1934, , 01/Jan-1951,f 25.Dec.1937 23/09/1973, 1/Feb/2016

# # output:
#
# Day: 13, Month: Jul, Year: 1928
# Day: 10, Month: Nov, Year: 1934
# Day: 25, Month: Dec, Year: 1937


# pattern = "\\b(?P<day>\\d{2})([-.\\/])(?P<month>[A-Z]
# [a-z]{2})\\2(?P<year>\\d{4})\\b"
# text = input()
# matches = re.finditer(pattern, text)
# for match in matches:
#  print(f"Day: {match.group('day')}, Month:
# {match.group('month')}, Year: {match.group('year')}")
