
# https://pastebin.com/S68a8TpQ?fbclid=IwZXh0bgNhZW0CMTAAAR3Ps3mSpeYIFQ1gLWA2CW0ObeyvbiuYzOnUsxOI7YWhjSy1Ypz_SKcpqLw_aem_2NnJ5dk24RCsMoSI0hMVsw#google_vignette

chars = [char for char in input() if char != " "]
letters = {}

for char in chars:
    if char not in letters.keys():
        letters[char] = 0
    letters[char] += 1

for symbol, occurrences in letters.items():
    print(f"{symbol} -> {occurrences}")

# --------------
print(chars)

# # input:
# text text text

# # result:
# t -> 6
# e -> 3
# x -> 3


# ------------------------------

characters = [character for character in input() if character != " "]
letters = {}
for character in characters:
    if character not in letters.keys():  # if character not in letters
        letters[character] = 0
    letters[character] += 1
for symbol, occurrences in letters.items():
    print(f"{symbol} -> {occurrences}")
