deposit_sum = float(input())
term_deposit = int(input())
#percent_month = (float(input()) / 100) / 12
percent_month = float(input()) / 100

#sum = deposit_sum + term_deposit * (deposit_sum * percent_month)
sum = deposit_sum + term_deposit * ((deposit_sum * percent_month) / 12)

print(sum)
