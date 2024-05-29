
text = input()
index = []

for i in range(len(text)):
    if text[i].isupper():
        index.append(i)
print(index)

