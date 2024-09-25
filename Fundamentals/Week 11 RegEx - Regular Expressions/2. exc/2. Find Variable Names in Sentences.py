import re

text = input()

pattern = r"\b_([A-Za-z0-9]+)\b"
matches = re.findall(pattern, text)
print(",".join(matches))

# # input:
#
# Calculate the _area of the _perfectRectangle object.

# # output:
#
# area,perfectRectangle
