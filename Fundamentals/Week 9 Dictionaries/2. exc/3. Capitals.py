
country_lst = input().split(", ")
city_lst = input().split(", ")

capitals_d = dict(zip(country_lst, city_lst))

for country, city in capitals_d.items():
    print(f"{country} -> {city}")

# # input:
#
# Bulgaria, Romania, Germany, England
# Sofia, Bucharest, Berlin, London

# # result:
#
# Bulgaria -> Sofia
# Romania -> Bucharest
# Germany -> Berlin
# England -> London
