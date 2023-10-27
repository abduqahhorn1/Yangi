n = int(input("N ga qiymat bering: "))
a = 0
while n != 0:
    if n % 10 == 2:
        a += 1
    n //= 10
print(a,"ta")