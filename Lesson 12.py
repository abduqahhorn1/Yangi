# w - write , create , rewrite
# r - read  , not found error
# a - append , create , append
# t - text
# b - binary


# f = open("data.txt","r")
# d = f.readlines()[-1]
# i = int(d.split("-")[0])
# print(i)
# f = open("data.txt", "a")
# while True:
#     i+=1
#     n = input("So'z kiriting: ")
#     if n=="stop": break
#     f.write(f"{i}-qator: {n}\n")
# f.close()

# i = 1
# while i!=11:
#   n = input("So'z kiriting ")
#   f.write(f"\n{i}-qator: {n}")
#   i+=1
# f.close() 
for i in range(1 ,6):
    f = open(f"{i}.txt","a")
    f.close()