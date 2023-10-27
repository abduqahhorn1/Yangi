n = int(input("N ga qiymat bering: "))
i = 0;  a = 0
while n != 0:
    i += n % 10
    a += 1
    n //= 10
print("Raqmlari yig'indisi: ",i,)
print("Raqmlari soni: ",a)
