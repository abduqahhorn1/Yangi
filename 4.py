def largest_of_three(a, b, c):

    if a == b == c:
        return a
    elif a == b or a == c:
        return a
    elif b == c:
        return b
    
    else:
        max_num = a
        if b > max_num:
            max_num = b
        if c > max_num:
            max_num = c
        return max_num
a = 10
b = 5
c = 20
max_num = largest_of_three(a, b, c)
print(max_num)