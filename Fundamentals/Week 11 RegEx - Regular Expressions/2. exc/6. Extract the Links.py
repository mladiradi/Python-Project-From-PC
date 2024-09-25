
import re

text = input()
pattern = r"(w{3}\.[A-Za-z0-9-]+(\.[a-z]+)+)"

while text:
    match = re.search(pattern, text)
    if match:
        url = match.group(1)
        print(url)
    text = input()

# # input:
#
# Join WebStars now for free, at www.web-stars.com
# You can also support our partners:
# Internet - www.internet.com
# WebSpiders - www.webspiders101.com
# Sentinel - www.sentinel.-ko

# # output:
#
# www.web-stars.com
# www.internet.com
# www.webspiders101.com
