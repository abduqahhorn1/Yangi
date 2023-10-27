def txt_fayldagi_matnlarni_ekrangacha_chiqarish(fayl_nomi):
    try:
        with open(fayl_nomi, 'r') as file:
            matnlar = file.readlines()
            for matn in matnlar:
                print(matn.strip())
    except Exception as e:
        print("Xatolik yuz berdi:", e)

fayl_nomi = input("TXT fayl nomini kiriting: ")

txt_fayldagi_matnlarni_ekrangacha_chiqarish(fayl_nomi)