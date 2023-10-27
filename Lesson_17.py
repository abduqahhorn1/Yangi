# import tkinter
# from tkinter import messagebox

# window = tkinter.Tk()
# window.geometry("300x200")
# window.title("Register")

# def lastId():
#     last_id = 1
#     with open("user.txt" , "r") as f:
#         lines = f.readlines()
#         if len(lines) == 0:
#             return last_id
#         last_line = lines[-1]
#         last = last_line.split('.')[0]
#         return int(last) + last_id



# def get_data():
#     name = name_input.get()
#     lastname = lastname_input.get()
#     print(name,lastname)
#     if len(name) == 0 or len(lastname) ==0:
#        messagebox.showerror("Xatolik", "Ism yoki familya kiritilmadi")
#     else:
#       last_id = lastId()
#       with open("user.txt" , "a") as f:
#         f.write(f"{last_id}.{name} {lastname}\n")

# name_1 = tkinter.Label(window ,text="Ismingiz", font=("times", 15, "bold"))
# name_1.grid(row=0 , column=0)

# name_input = tkinter.Entry()
# name_input.grid(row=0, column=1)

# lastname_1 = tkinter.Label(window ,text="Familyangiz", font=("times", 15, "bold"))
# lastname_1.grid(row=1 , column=0)

# lastname_input = tkinter.Entry()
# lastname_input.grid(row=1, column=1)

# button = tkinter.Button( text="Ro'yxatga olish",bg="yellow", command=get_data )
# button.grid(row=2 , column=1)




# window.mainloop()




class MobilePhone:

    def __init__(self,number,owner) -> None:
        self.number = number
        self.owner = owner

    def output_call(self, target):
        print(f"{self.owner} telefon qilyabdi {target} ga telefon qilyabdi")


class Operator:

    def __init__(self,number,owner) -> None:
        self.number = number
        self.owner = owner

    def output_call(self, target):
        print(f"{self.owner} telefon qilyabdi {target} ga telefon qilyabdi")

mobile = MobilePhone(998991234567, "Saloxiddin")
MobilePhone.output_call(mobile, "Sherali")