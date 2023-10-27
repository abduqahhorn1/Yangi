def copy_list(tup):
    lst = list(tup) 
    return lst


tup = (1, 2, 3, 4, 5)

lst = copy_list(tup)

print(lst)  # [1, 2, 3, 4, 5]