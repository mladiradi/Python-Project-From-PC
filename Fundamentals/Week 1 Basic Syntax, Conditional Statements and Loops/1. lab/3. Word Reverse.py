
text = input()

rev_text = ''

for i in range(len(text)-1, -1, -1):
    rev_text += text[i]

print(rev_text)
