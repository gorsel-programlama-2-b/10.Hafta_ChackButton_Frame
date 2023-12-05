# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 13:49:12 2023

@author: C-117
"""

from tkinter import*


pencere = Tk()
pencere.tk_setPalette("#CECEF6")

cerceve1=Frame(bg="Green",
               height=500,
               width=500,
               bd=10)
cerceve1.grid(row=0, column=0, pady=5, padx=5)

cerceve2=Frame(bg="Blue",
               height=500,
               width=500,
               bd=10)
cerceve2.grid(row=1, column=0, pady=10, padx=10)

cerceve3=Frame(bg="Black",
               height=500,
               width=500,
               bd=10)
cerceve3.grid(row=0, column=1, pady=5, padx=5)

cerceve4=Frame(bg="Pink",
               height=500,
               width=500,
               bd=10)
cerceve4.grid(row=1, column=1
              , pady=10, padx=10)

button1 = Button(cerceve1, text="Button 1",
                 height=25,
                 width=25,
                 bd=5)
button1.pack(pady=1, padx=1)

chackbutton1 = Checkbutton(cerceve2, text="beşiktaşk", 
                 height=25,
                 width=25,
                 bd=5)
chackbutton1.pack(pady=10, padx=10)

button3 = Button(cerceve3, text="Button 3",
                 height=25,
                 width=25,
                 bd=5)
button3.pack(pady=10, padx=10)

button4 = Button(cerceve4, text="Button 4",
                 height=25,
                 width=25,
                 bd=5)
button4.pack(pady=10, padx=10)


pencere.mainloop()