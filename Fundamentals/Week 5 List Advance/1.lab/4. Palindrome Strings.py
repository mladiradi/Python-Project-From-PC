

words_input = input().split()
palindrom = input()

palindrom_list = [word for word in words_input if word == word[::-1]]
palindrom_counter = palindrom_list.count(palindrom)

print(palindrom_list)
print(f'Found palindrome {palindrom_counter} times')

# обикновен цикъл вместо list comprehension
# for word in words_input:
#     if word == word[::-1]
#         palindrom_list.append(word)
