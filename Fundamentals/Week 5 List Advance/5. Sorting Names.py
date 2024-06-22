
def sort_names(names_list):
    return sorted(names_list, key=lambda name: (-len(name), name))
    #  първо сортираме по броя на символите от думата с най-много символи към по-малко(-len(name))
    #  после с (, name) сортираме по азбучен ред
    # key=lambda name: - за name се взима (x) всеки индекс от names_list


names_lst = input().split(", ")
result = sort_names(names_lst)
print(result)
