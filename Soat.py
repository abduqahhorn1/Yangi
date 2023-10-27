import tkinter
import time
window = tkinter.Tk()

window.geometry("600x320")
def soat():
  time_string = time.strftime("%H:%M:%S")
  date = time.strftime("%Y.%m.%d")
  label.config(text=f"{time_string} \n {date}")
  label.after(1000,soat)

label = tkinter.Label(
    window, font=("times", 75 , "bold"),bg="yellow"
)


label.grid( row=2, column=1, padx=50,pady=25)


soat()
window.mainloop()
