a = int(input("a ga qiymat kiriting: "))
b = int(input("b ga qiymat kiriting: "))
if a != b:
    a = a + b
    b = a
else:
    a = 0
    b = 0
print("a:", a)
print("b:", b)