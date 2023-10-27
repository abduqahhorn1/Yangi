# import random

# reset = 2315

# print( random.randint(1000, 10000))
# def helpjumavoy(minutes):
#     count = 0
#     while count < minutes * 60:
# 


# d = {}

# for i in range(1,11):
#     d[f"number_{i}"] = i
#     print(d) 
#     for i in d:
#         d[i] = 0
# print(d)

savollar =  dict(
    savol1="Osmon rangi qanaqa",savol2="Xitoy poxtatxi qayer",savol3="Qozon rangi",savol4="Yerning shakli",
    savol5= "5*5 nechaga teng",savol6="O'zbekiston poytaxti qayer",savol7=""

)
javoblar = dict(
   a="Qizil", b="Sap sariq", c="Moviy", d="Bilmasam",                                
   a1="Guanjo", b1="Shanxay", c1="Texas", d1="Pekin",
   a2="Qizil", b2="Qora", c2="Yashil", d2="Oppoq",
   a3="Dumaloq", b3="Kvadrat", c3="Romb", d3="Qayerda u yer"
)
score = 0
name = input("Ismingiz: ")
print(f"Assalomu aleykum {name}. Xozir sizga savollar beraman. To'g'ri javobni kiritasiz")
for q in savollar:
    print(q)
    i = "savollar.(q)"
    variant = "javoblar"
    for v in variant:
        if v != "true_answer":
            print(f"{v}. [variant{v}]")
    answer = input("Javob variantini tanlang: ")
    if answer == variant['true_answer']:score += 1

print(f"Siz {len(savollar)} ta savoldan {score} ta topdingiz ")

