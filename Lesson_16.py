import tkinter

window = tkinter.Tk()  # Tk class object

window.geometry("250x250")  # object method
window.title("Counter")  # object method
window.counter = 0
def clicked():
    window.counter +=1
    label.config(text=f"{window.counter}")

window.counter = 0
def clicked1():
    window.counter -=1
    label.config(text=f"{window.counter}")


label = tkinter.Label(window, text="Start" , font=("times", 50, "bold" ))
label.pack(fill="both", expand=True)

button = tkinter.Button(window, text="Click me +",bg="green" , command=clicked)
button.pack(fill="both", expand=True)

button = tkinter.Button(window, text="Click me -",bg="red" , command=clicked1)
button.pack(fill="both", expand=True)

window.mainloop()



# class Rect:
#     MIN = 1
#     MAX = 100

#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     @classmethod
#     def check_param(cls, a, b):
#         if isinstance(a, int) and isinstance(b, int):
#             if (cls.MIN <= a <= cls.MAX) and (cls.MIN <= b <= cls.MAX):
#                 return True
#         return False

#     @staticmethod
#     def area(a, b):
#         return a * b


# rect = Rect(a=3, b=8)
# rect.MIN = 300
# print(Rect.check_param(a=34, b=45))


# class Triangle:
#     def __init__(self,a,b,c) -> None:
#         self.a = a
#         self.b = b
#         self.c = c
#     @classmethod
#     def check_triangle(cls,a,b,c):
#         if isinstance(a,int) and isinstance(b,int) and isinstance(c,int):
#             return True
#         else:
#             return False
        
#     @staticmethod
#     def area(a,b,c):
#         if Triangle.check_triangle(a,b,c):
#             return a * b * c
#         else:
#             raise ValueError("Xato")
        
# Triangle = Triangle(a=3, b=8 ,c=5)
# print(Triangle)