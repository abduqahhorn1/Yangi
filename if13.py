a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
c = float(input("Uchinchi sonni kiriting: "))
if a > b and a > c:
    i = a
    if b > c:
        y = b
    else:
        y = c
elif b > a and b > c:
    i = b
    if a > c:
        y = a
    else:
        y = c
else:
    i = c
    if a > b:
        y = a
    else:
        o = b
print("O'rtadagi son:", y)