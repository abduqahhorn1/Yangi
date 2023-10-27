def sum_list(lst):
    total = 0
    for a in lst:
        if isinstance(a, (int, float)):
            total += a
    return total


lst = [1, 2, 3, 4, 5, 2.5]


print(sum_list(lst))  