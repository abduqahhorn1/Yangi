# import tkinter
# import time
# window = tkinter.Tk()

# window.geometry("600x320")
# def my_time():
#   time_string = time.strftime("%H:%M:%S")
#   date = time.strftime("%Y.%m.%d")
#   label.config(text=f"{time_string} \n {date}")
#   label.after(1000,my_time)

# label = tkinter.Label(
#     window, font=("times", 75 , "bold"),bg="yellow"
# )


# label.grid( row=2, column=1, padx=50,pady=25)


# my_time()
# window.mainloop()

class Car:
    def __init__(self,model,color,power,year, km):
        self.model = model
        self.color = color
        self.power = power
        self.year = year
        self.km = km
        self.seriaNumer = 235456
    def set_color(self,new_color):
        if type(new_color) == str and new_color in ["white","red","blue"]:
          self.color = new_color
        return self.color
    raise ValueError("Invalid color")
    



tico = Car("Dewoo","white","48","1998","km=450000")
# tico.color = "black"
tico.set_color = 7
print(tico.color)

