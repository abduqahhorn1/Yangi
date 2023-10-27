a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))

summa_kvadratlar = 0
for i in range(a, b+1):
    summa_kvadratlar += i ** 2

print(f"{a} dan {b} gacha bo'lgan sonlar kvadratlarining yig'indisi: {summa_kvadratlar}")