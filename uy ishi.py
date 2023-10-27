savollar = {
    "Qaysi davlatning poytaxti London?": {"a": "Germaniya", "b": "Angliya", "c": "Fransiya", "d": "Rossiya", "javob": "b"},
    "Quyidagi sonlardan eng katta qaysi?": {"a": "0", "b": "1", "c": "-1", "d": "0.5", "javob": "d"},
    "7 x 7 nechiga teng?": {"a": "14", "b": "48", "c": "49", "d": "56", "javob": "c"},
    "Quyidagi hayvonlardan qaysi qorniga ega emas?": {"a": "Sigir", "b": "Qo'rg'on", "c": "Ovta", "d": "To'ngiz", "javob": "d"},
    "Quyidagi olam tili qaysi davlatda gaplashiladi?": {"a": "Mandarin", "b": "Yapon", "c": "Fransuz", "d": "Ispan", "javob": "a"},
    "Quyidagi ranglardan qaysi 'primarniy' rang emas?": {"a": "Qora", "b": "Oq", "c": "Yashil", "d": "Ko'k", "javob": "a"},
    "Quyidagi kitoblaridan qaysi Harry Potter kitobidir?": {"a": "The Lord of the Rings", "b": "The Hunger Games", "c": "The Da Vinci Code", "d": "Harry Potter and the Philosopher's Stone", "javob": "d"},
    "Quyidagi yillarning qaysi yili Kabisa yili hisoblanadi?": {"a": "2020", "b": "2024", "c": "2028", "d": "2032", "javob": "b"},
    "Quyidagi elementlardan qaysi g'ovakli metaldan tuzilgan?": {"a": "Aluminiy", "b": "Zomorf", "c": "Qalay", "d": "Temir", "javob": "a"},
    "Quyidagi sonlar qatorining yig'indisi qaysi? 1, 3, 5, 7, 9, 11, 13, 15, 17, 19": {"a": "90", "b": "95", "c": "100", "d": "105", "javob": "b"}
}

togri_javoblar_soni = 0
notogri_javoblar_soni = 0

for savol, javoblar in savollar.items():
    print(savol)
    for variant, javob in javoblar.items():
        if variant == "javob":
            continue
        print(f"{variant}) {javob}")
    javob_kirit = input("Javobingizni kiriting: ")
    if javob_kirit.lower() == javoblar["javob"].lower():
        print("To'g'ri!")
        togri_javoblar_soni += 1
    else:
        print("Noto'g'ri!")
        notogri_javoblar_soni += 1

bal = togri_javoblar_soni * 5
print(f"Test natijalari:\nTo'g'ri javoblar soni: {togri_javoblar_soni}\nNoto'g'ri javoblar soni: {notogri_javoblar_soni}\nJami ball: {bal}")