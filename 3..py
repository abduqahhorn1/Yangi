def sumDict(d):
    total = 0
    for key in d:
        if isinstance(d[key], int):
            total += d[key]
    return total

d = {'number_1': 1, 'name': 'Olim', 'email': 'Email', 'number_2': 2, 'number_3': 3, 'number_4': 4}

result = sumDict(d)
print(result)