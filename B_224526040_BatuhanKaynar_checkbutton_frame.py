# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 13:48:38 2023

@author: C-117
"""
from tkinter import * 
import tkinter as tk 
from tkinter import ttk

pencere = Tk()


frame1 = Frame(bg="green",
               height=200,
               width=200,
               bd=50)
frame1.grid(row=0, column=0, pady=5, padx=5)

frame2 = Frame(bg="blue",
                    height=200,
                    width=200,
                    bd=50)
frame2.grid(row=0, column=1, pady=5, padx=5)

frame3 = Frame(bg="red",
                    height=200,
                    width=200,
                    bd=50)
frame3.grid(row=1, column=0, pady=5, padx=5)                        
            
frame4 = Frame(bg="white",
                    height=200,
                    width=200,
                    bd=50)
frame4.grid(row=1, column=1, pady=5, padx=5)              
            
buton1 = Button(frame1, text="emircan")
buton1.grid(row=1, column=0)
            
chkbtn1 =Checkbutton(frame1, text="turp")
chkbtn1.grid(row=0, column=0)


chkbtn2 =Checkbutton(frame2, text="armut")
chkbtn2.grid(row=0, column=0)

entry=Entry(frame2)
entry.grid(row=1, column=0)


chkbtn3 =Checkbutton(frame3, text="karpuz")
chkbtn3.grid(row=0, column=0)

cmb=ttk.Combobox(frame3, values=["avrupa","afrika","amerika","asya"])
cmb.grid(row=1, column=0)














chkbtn4 =Checkbutton(frame4, text="muz")
chkbtn4.grid(row=0, column=0)



























pencere.mainloop()





























