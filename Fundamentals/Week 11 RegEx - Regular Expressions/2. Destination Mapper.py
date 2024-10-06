import re

result = []
points = 0

text = input()
pattern = r'(=|\/)([A-Z][a-zA-Z]{2,})\1'
matches = re.findall(pattern, text)

for match in matches:
    for i in range(len(match[1])):
        points += 1
    result.append(match[1])

print(f"Destinations: {', '.join(result)}")
print(f"Travel Points: {points}")

# # input:
#
# =Hawai=/Cyprus/=Invalid/invalid==i5valid=/I5valid/=i=

# # output:
#
# Destinations: Hawai, Cyprus
# Travel Points: 11

text = input()
pattern = r'(=|\/)([A-Z][a-zA-Z]{2,})\1'
matches = re.findall(pattern, text)
destinations = [match[1] for match in matches]
points = sum(len(destination) for destination in destinations)
print(f"Destinationd: {', '.join(destinations)}\nTravel Points: {points}")
