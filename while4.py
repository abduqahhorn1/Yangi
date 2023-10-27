n = int(input("N ga qiymat bering: "))
x = 0
y = 1
while n > x:
    x = 3**y
    y += 1
if n == 3**(y-1):
    print("3-ning darajasi")
else:
    print("3 ning darajasi emas")