
def common_elements(t1, t2):
    t1 = (1, 2, 3, 4, 5)
    t2 = (3, 4, 5, 6, 7)

    
    set1 = set(t1)
    set2 = set(t2)
    return list(set1 & set2)
print(common_elements)
