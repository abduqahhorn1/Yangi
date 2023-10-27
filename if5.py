a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
c = int(input("Uchinchi sonni kiriting: "))
i=0
y=0
if a>0:
    i+=1
elif a<0:
    y+=1
if b>0:
    i+=1
elif b<0:
    y+=1
if c>0:
    i+=1
elif c<0:
    y+=1
print("Musbat sonlar:",i)
print("Manfiy sonlar:",y)
