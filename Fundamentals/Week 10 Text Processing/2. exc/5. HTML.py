
title = input().strip()
content = input().strip()

html_output = f"<h1>\n    {title}\n</h1>\n"
html_output += f"<article>\n    {content}\n</article>\n"

while True:
    line = input().strip()
    if line == "end of comments":
        break
    html_output += f"<div>\n    {line}\n</div>\n"

print(html_output)
