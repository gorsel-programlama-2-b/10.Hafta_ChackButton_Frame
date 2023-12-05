from tkinter import *
from tkinter.ttk import Combobox

pencere = Tk()
pencere.geometry("750x750")

cerceve1 = Frame(bg="green",height=300,width=300)
cerceve1.grid(row=0, column=0, pady=5,padx=5)

boton = Button(cerceve1,text="tıkla",)
boton.grid(row=1, column=1, pady=90,padx=90)

check1 = Checkbutton(cerceve1,text= "bir")
check1.grid(row=0, column=1, pady=90,padx=90)

cerceve2 = Frame(bg="blue",height=300,width=300)
cerceve2.grid(row=0, column=1, pady=5,padx=5)

check2 = Checkbutton(cerceve2,text= "iki")
check2.grid(row=1, column=1, pady=90,padx=90)

entry = Entry(cerceve2)
entry.grid(row=2, column=1, pady=90,padx=90)

cerceve3 = Frame(bg="orange",height=350,width=350)
cerceve3.grid(row=1, column=1, pady=5,padx=5)




cerceve4 = Frame(bg="red",height=350,width=350)
cerceve4.grid(row=1, column=0, pady=5,padx=5)

check4 = Checkbutton(cerceve3,text= "ilk")
check4.grid(row=1, column=0, pady=150,padx=150)

combo = Combobox(cerceve4,values=["domates","biber","çeri domartes"])
combo.grid(row=1, column=1, pady=90,padx=90)

check3 = Checkbutton(cerceve4,text= "ilk")
check3.grid(row=0, column=1, pady=90,padx=90)

pencere.mainloop()