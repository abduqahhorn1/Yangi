products = {
    "olma":{"price":10000, "remainer":21},
    "limon":{"price":15000,"remainer":8},
    "banan":{"price":15000,"remainer":35},
    "kiwi":{"price":20000, "remainer":9},
    "shaftoli":{"price":5000, "remainer":40},
}


choice = input("Meva nomini kiriting: ")
choice.title()
all_summa = 0
if choice in products:
    print(f"{choice}bor 1 kg narxi {products[choice]}so'm")
    kg = input("Necha kg kerak: ") 
    if kg.isdigit():
        kg = int(kg)
        summa = kg * products[choice]
        print(f"{kg} kilosi {summa} so'm bo'ladi")
        s = input(f"Sotib olasizmi (yes/no): ")
    if s == "yes":
        all_summa += summa
        print("Haridingiz uchun rahmat")
        print(f"Bugungi tushum {summa} so'm")
    else:
        print(f"Kechirasiz {choice} do'konda yo'q")