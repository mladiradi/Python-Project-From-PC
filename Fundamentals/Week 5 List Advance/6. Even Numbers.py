
num_lest = list(map(int, input().split(", ")))

fund_ivans = map(lambda x: x if num_lest[x] % 2 == 0 else 'no', range(len(num_lest)))
express_ivans = list(filter(lambda x: x != 'no', fund_ivans))
print(express_ivans)
