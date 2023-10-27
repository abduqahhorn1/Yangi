N = int(input("N ga qiymat bering: "))
K = int(input("K ga qiymat bering: "))
a = 0
while N >= 0:
    N -= K
    a += 1
print("Butun qism: ",a-1)
print("Qoldiq qism: ",N+K)