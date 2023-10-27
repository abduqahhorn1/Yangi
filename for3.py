a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))

count = 0
for i in range(b-1, a, -1):
    print(i)
    count += 1

print(f"Natijada {count} ta son chiqarildi.")