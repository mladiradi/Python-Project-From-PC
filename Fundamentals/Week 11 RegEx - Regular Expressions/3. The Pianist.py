
number = int(input())
collection = {}

for i in range(number):
    piece_info = input().split('|')
    piece = piece_info[0]
    composer = piece_info[1]
    key = piece_info[2]
    collection[piece] = {'composer': composer, 'key': key}

while True:
    command = input()
    if command == 'Stop':
        break

    command_parts = command.split('|')
    current_action = command_parts[0]
    if current_action == 'Add':
        piece = command_parts[1]
        composer = command_parts[2]
        key = command_parts[3]

        if piece in collection:
            print(f"{piece} is already in the collection!")
        else:
            collection[piece] = {'composer': composer, 'key': key}
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif current_action == 'Remove':
        piece = command_parts[1]
        if piece in collection:
            del collection[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif current_action == 'ChangeKey':
        piece = command_parts[1]
        new_key = command_parts[2]
        if piece in collection:
            collection[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece, info in collection.items():
    print(f"{piece} -> Composer: {info['composer']}, Key: {info['key']}")


# # input:
#
# 4
# Eine kleine Nachtmusik|Mozart|G Major
# La Campanella|Liszt|G# Minor
# The Marriage of Figaro|Mozart|G Major
# Hungarian Dance No.5|Brahms|G Minor
# Add|Spring|Vivaldi|E Major
# Remove|The Marriage of Figaro
# Remove|Turkish March
# ChangeKey|Spring|C Major
# Add|Nocturne|Chopin|C# Minor
# Stop

# # output:
#
# Spring by Vivaldi in E Major added to the collection!
# Successfully removed The Marriage of Figaro!
# Invalid operation! Turkish March does not exist in the collection.
# Changed the key of Spring to C Major!
# Nocturne by Chopin in C# Minor added to the collection!
# Eine kleine Nachtmusik -> Composer: Mozart, Key: G Major
# La Campanella -> Composer: Liszt, Key: G# Minor
# Hungarian Dance No.5 -> Composer: Brahms, Key: G Minor
# Spring -> Composer: Vivaldi, Key: C Major
# Nocturne -> Composer: Chopin, Key: C# Minor
