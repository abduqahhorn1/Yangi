def satrlarni_faylga_yozish(satrlar):
    try:
        with open("index.txt", "w") as file:
            for satr in satrlar:
                file.write(satr + "\n")
        print("Satrlar faylga yozildi.")
    except Exception as e:
        print("Xatolik yuz berdi:", e)

satrlar = ["Bu birinchi satr.", "Ikkinchi satr.", "Uchunchi satr."]

satrlarni_faylga_yozish(satrlar)