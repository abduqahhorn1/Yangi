n = int(input("N ga qiymat bering: "))
m = int(input("M ga qiymat bering: "))
N= n;  a = 0;  b = 0
while N >= 0:
    N -= m
    a += 1
print("Butun qism: ",a-1,"\nQoldiq qism: ",N+m)