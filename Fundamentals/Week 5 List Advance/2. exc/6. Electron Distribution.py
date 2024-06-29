
number = int(input())
shell_list = []
i = 0

while 0 < number:

    i += 1
    shell = 2 * (i ** 2)

    if number >= shell:
        shell_list.append(shell)
        number -= shell
    else:
        shell_list.append(number)
        number = 0

print(shell_list)
