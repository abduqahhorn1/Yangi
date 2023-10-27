a = int(input("a ga qiymat kiriting: "))
b = int(input("b ga qiymat kiriting: "))
if a != b:
    if a > b:
        b = a
    else:
        a = b
else:
    a = 0
    b = 0
print("a:", a)
print("b:", b)