# phone = "+998901234567"


# def checkNumber(phone:str) -> bool:
#     assert len(phone) == 13 ,"Telefon raqamiz xato"
#     assert phone.startswith("+99890") or phone.startswith("+99891")
#     assert phone[6:].isdigit() ,"Telefon raqamingiz xato"
# r = checkNumber(phone)
# print("phone")

# summa = 0
# while True:
#    x = input("Son kiriting /stop: ")
#    try:
#       x=int(x)
#    except:
#       print("Xatolik")
#    else:
#       summa += x
#    if x=="stop":break
# print(summa)

import random
l = list(range(1,16))
l2 = random.sample(1,5)
print(l2)

