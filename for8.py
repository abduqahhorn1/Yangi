a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))

kopaytma = 1
for i in range(a, b+1):
    kopaytma *= i

print(f"{a} dan {b} gacha bo'lgan sonlarning ko'paytmasi: {kopaytma}")