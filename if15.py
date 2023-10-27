a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
c = int(input("Uchinchi sonni kiriting: "))
x = a + b
y = a + b
z = b + c
if x > y and x > z:
    print("Eng katta yig'indi:", a, "va", b)
elif y > x and y > z:
    print("Eng katta yig'indi:", a, "va", c)
else:
    print("Eng katta yig'indi:", b, "va", c)