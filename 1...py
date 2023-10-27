def difference_list(list1, list2):
    
    set1 = set(list1)
    set2 = set(list2)
    return list(set1 - set2)
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
print(difference_list)