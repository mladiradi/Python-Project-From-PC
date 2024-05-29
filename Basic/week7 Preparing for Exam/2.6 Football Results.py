
result_1st = input()
result_2nd = input()
result_3rd = input()

win = 0
lost = 0
even = 0

if ord(result_1st[0]) > ord(result_1st[2]):
    win += 1
elif ord(result_1st[0]) < ord(result_1st[2]):
    lost += 1
else:
    even += 1

if ord(result_2nd[0]) > ord(result_2nd[2]):
    win += 1
elif ord(result_2nd[0]) < ord(result_2nd[2]):
    lost += 1
else:
    even += 1

if ord(result_3rd[0]) > ord(result_3rd[2]):
    win += 1
elif ord(result_3rd[0]) < ord(result_3rd[2]):
    lost += 1
else:
    even += 1

print(f"Team won {win} games.")
print(f"Team lost {lost} games.")
print(f"Drawn games: {even}")

# result1 = input()
# result2 = input()
# result3 = input()
# count_w = 0
# count_d = 0
# count_l = 0
#
# d_result1 = result1[0:1]
# g_result1 = result1[-1]
# if d_result1 > g_result1:
#     count_w += 1
# elif d_result1 < g_result1:
#     count_l += 1
# else:
#     count_d += 1
#
# d_result2 = result2[0:1]
# g_result2 = result2[-1]
# if d_result2 > g_result2:
#     count_w += 1
# elif d_result2 < g_result2:
#     count_l += 1
# else:
#     count_d += 1
#
# d_result3 = result3[0:1]
# g_result3 = result3[-1]
# if d_result3 > g_result3:
#     count_w += 1
# elif d_result3 < g_result3:
#     count_l += 1
# else:
#     count_d += 1
#
# print(f'Team won {count_w:.0f} games.\nTeam lost {count_l:.0f} games.\nDrawn games: {count_d:.0f}')
