
deck_of_cards = input().split()
count_of_shuffles = int(input())

for shuffle in range(count_of_shuffles):
    middle_of_the_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[:middle_of_the_deck]
    right_part = deck_of_cards[middle_of_the_deck:]
    deck_after_shuffling = []

    for card_index in range(len(left_part)): # len(right_part)
        deck_after_shuffling.append(left_part[card_index])
        deck_after_shuffling.append(right_part[card_index])
    deck_of_cards = deck_after_shuffling

print(deck_of_cards)

# lst_of_cards = input().split()
# shuffles_num = int(input())
#
# left_deck = []
# right_deck = []
#
# for i in range(shuffles_num):
#     for deck in range(len(lst_of_cards)):
#         if deck < (len(lst_of_cards) // 2):
#             left_deck.append(lst_of_cards[deck])
#         else:
#             right_deck.append(lst_of_cards[deck])
#     sum_lst = []
#     for ii in range(len(left_deck)):
#         sum_lst.append(str(left_deck[ii]))
#         sum_lst.append(str(right_deck[ii]))
#     lst_of_cards = sum_lst
#     left_deck = []
#     right_deck = []
#
# print(lst_of_cards)
