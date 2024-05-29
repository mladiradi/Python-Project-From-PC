
book_name = input()

counter = 0

while True:

    library_book = input()

    if book_name == library_book:
        print(f'You checked {counter} books and found it.')
        break

    if library_book == 'No More Books':
        print(f'The book you search is not here!')
        print(f'You checked {counter} books.')
        break

    counter += 1
