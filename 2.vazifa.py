def aylantirish_int(malumot):
    try:
        aylanadi = int(malumot)
        print("Aylanadi:", aylanadi)
    except ValueError:
        print("Xatolik yuz berdi. Ma'lumotni int ga aylantirib bo'lmaydi.")

kiruvchi_malumot = input("Ma'lumotni kiriting: ")
aylantirish_int(kiruvchi_malumot)