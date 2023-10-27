import csv

def malumotlarni_saqlash(tovar_nomi, narxi, rangi, soni):
    try:
        with open('malumotlar.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([tovar_nomi, narxi, rangi, soni])
        print("Ma'lumotlar CSV faylga saqlandi.")
    except Exception as e:
        print("Xatolik yuz berdi:", e)

# Kiruvchi ma'lumotlarni olish
tovar_nomi = input("Tovar nomini kiriting: ")
narxi = input("Tovar narxini kiriting: ")
rangi = input("Tovar rangini kiriting: ")
soni = input("Tovar sonini kiriting: ")

malumotlarni_saqlash(tovar_nomi, narxi, rangi, soni)