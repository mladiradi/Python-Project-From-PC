import re

text = input()
pattern = r'(=|\/)([A-Z][a-zA-Z]{2,})\1'
matches = re.findall(pattern, text)

destinations = [match[1] for match in matches]
points = sum(len(destination) for destination in destinations)

print(f"Destinations: {', '.join(destinations)}\nTravel Points: {points}")

