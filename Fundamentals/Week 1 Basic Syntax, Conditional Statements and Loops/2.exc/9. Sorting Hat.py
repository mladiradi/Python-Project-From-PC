
while True:
    counter = 0
    student_name = input()

    if student_name == 'Voldemort':
        print('You must not speak of that name!')
        break
    elif student_name == 'Welcome!':
        print(f'Welcome to Hogwarts.')
        break

    for char in student_name:
        counter += 1

    if counter < 5:
        print(f'{student_name} goes to Gryffindor.')
    elif counter == 5:
        print(f'{student_name} goes to Slytherin.')
    elif counter == 6:
        print(f'{student_name} goes to Ravenclaw.')
    else:
        print(f'{student_name} goes to Hufflepuff.')
