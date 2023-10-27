a = int(input("A ga qiymat kiriting: "))
b = int(input("B ga qiymat kiriting: "))

x = 0
while a>=b:
    a -= b
    x += 1
print(x)