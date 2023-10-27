# a = int(input("Son kiriting"))
# l = [0,1]
# for i in range(len(a)):
#     l.append(l[-1]+l[-2])
    
# print(l)


def factarial(n):
    if n ==1:
        return 1
    return n*factarial(n-1)
n = int(input("Son kiriting: "))
print(factarial(n))