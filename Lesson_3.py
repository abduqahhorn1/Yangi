# def outer():
#     x = 0
#     def inner():
#         nonlocal x
#         x += 1
#         print(x)

#     return inner

# def calculate(a:int,b:int):
#     def add():
#         nonlocal a,b
#         return a + b
#     def multiply():
#         nonlocal a,b
#         return a * b
#     def divide():
#         nonlocal a,b
#         return a / b
#     calculate.add = add
#     calculate.multiply = multiply
#     calculate.divide = divide
#     return calculate

# c = calculate(10,5)
# print(c.add())
    
def converter(a:int):
    x = a/12100
    return


    