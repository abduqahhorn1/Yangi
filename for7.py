a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))

summa = 0
for i in range(a, b+1):
    summa += i

print(f"{a} dan {b} gacha bo'lgan sonlarning yig'indisi: {summa}")