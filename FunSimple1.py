A = float(input("A ga qiymat kiriting: "))
B = float(input("B ga qiymat kiriting: "))
C = float(input("C ga qiymat kiriting: "))
D = int(input("D ga qiymat kiriting: "))
E = int(input("E ga qiymat kiriting: "))

def PowerA3(son):
    S = 1
    for i in range(3):
        S *= son
    return S

print(PowerA3(A))
print(PowerA3(B))
print(PowerA3(C))
print(PowerA3(D))
print(PowerA3(E))