n = int(input("N ga qiymat bering: "))
i = 10
j = 1
a = str(n%10)
while j < len(str(n)):    
    a += str((n//i)%10)
    i *= 10
    j += 1
print(a)
