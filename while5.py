n = int(input("N ga qiymat bering: "))
x = 0
y = 1
while n > x:
    x = 2**y
    y += 1
if n == 2**(y-1):
    print(y-1)
else:
    print("2 ning darajasi emas")