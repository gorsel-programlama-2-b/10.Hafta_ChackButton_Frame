from tkinter import Tk, Frame, Button, Entry
from tkinter import ttk

Pencere = Tk()

cerceve1 = Frame(Pencere, bg="green", bd=100, height=150, width=150)
cerceve1.grid(row=0, column=0, pady=5, padx=5)

cerceve2 = Frame(Pencere, bg="lightblue", bd=100, height=150, width=150)
cerceve2.grid(row=0, column=1, pady=5, padx=5)

cerceve3 = Frame(Pencere, bg="red", bd=100, height=150, width=150)
cerceve3.grid(row=1, column=0, pady=5, padx=5)

cerceve4 = Frame(Pencere, bg="white", bd=100, height=150, width=150)
cerceve4.grid(row=1, column=1, pady=5, padx=5)

button = Button(cerceve1, text='Button')
button.pack(side='bottom')

textbox = Entry(cerceve2, width=10, borderwidth=2)
textbox.pack(pady=10)

combo_box = ttk.Combobox(cerceve3, text=".....")
combo_box.pack()

check_btn1 = ttk.Checkbutton(cerceve1, text=".....")
check_btn1.pack()

check_btn2 = ttk.Checkbutton(cerceve2, text=".....")
check_btn2.pack()

check_btn3 = ttk.Checkbutton(cerceve3, text=".....")
check_btn3.pack()

check_btn4 = ttk.Checkbutton(cerceve4, text=".....")
check_btn4.pack()

Pencere.mainloop()
