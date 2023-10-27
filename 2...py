def maxNum(d):
    
    
    
    if not d:
        return None

    max_val = None
    for val in d.values():
        if isinstance(val, int):
            if max_val is None or val > max_val:
                max_val = val

    return max_val
my_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 'hello'} 
maxNum(my_dict)

