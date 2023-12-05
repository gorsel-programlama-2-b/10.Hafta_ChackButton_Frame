from tkinter import *
from tkinter import ttk
pencere = Tk()
pencere.title("Frame Oluşturma")
pencere.configure(background="Black")

cerceve1 = Frame(bg="Green",
                 
                 bd=10)
                 
cerceve1.columnconfigure(0,weight=1,uniform="x")
cerceve1.rowconfigure((0,1),weight=1,uniform="x")
cerceve1_check = Checkbutton(cerceve1,text="Elma")
cerceve1_check.grid(row=0,column=0, pady=0, padx=0)
cerceve1_btn = Button(cerceve1,text="Frame1")
cerceve1_btn.grid(row=1, column=0, pady=5, padx=5)
cerceve1.grid(row=0 ,column=0, pady=5 , padx=5,sticky="nwse")


cerceve2 = Frame(bg="Blue",
                 bd=10)
cerceve2.columnconfigure(0,weight=1,uniform="x")
cerceve2.rowconfigure((0,1),weight=1,uniform="x")
cerceve2_ent = Entry(cerceve2)
cerceve2_check = Checkbutton(cerceve2,text="Kiraz")
cerceve2_check.grid(row=0,column=0, pady=0, padx=0)
cerceve2_ent.grid(row=1, column=0, pady=10, padx=10)
cerceve2.grid(row=0, column=1, pady=10 , padx=10)

cerceve3 = Frame(bg="Red",
                 bd=10)
cerceve3.columnconfigure(0,weight=1,uniform="x")
cerceve3.rowconfigure((0,1),weight=1,uniform="x")
cerceve3_check = Checkbutton(cerceve3,text="Şeftali")
cerceve3_check.grid(row=0,column=0, pady=0, padx=0)
cerceve3_box = ttk.Combobox(cerceve3,values=["Salatalık","Domates","Biber"])
cerceve3_box.grid(row=1, column=0, pady=15, padx=15)
cerceve3.grid(row=1,column=0, pady=15 , padx=15)

cerceve4 = Frame(bg="White",bd=10)
cerceve4.columnconfigure(0,weight=1,uniform="x")
cerceve4.rowconfigure((0,1),weight=1,uniform="x")
cerceve4_check = Checkbutton(cerceve4,text="Muz")
cerceve4_check.grid(row=0,column=0, pady=0, padx=0)
cerceve4.grid(row=1, column=1, pady=20 , padx=20)



pencere.mainloop()