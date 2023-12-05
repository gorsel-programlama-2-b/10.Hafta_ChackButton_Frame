# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 13:46:33 2023

@author: C-117
"""

from tkinter import Tk
from tkinter import *
from tkinter import ttk

pencere=Tk()



cerceve=Frame(bg="green",bd="100",height=250,width=250)
cercevebtn=Button(cerceve,text="Bas")
cercevechek=Checkbutton(cerceve,text="24. şampiyonluk")
cercevechek.grid(row=0,column=0)
cercevebtn.grid(row=1,column=0,)
cerceve.grid(row=0,column=0,padx=5,pady=5)

cerceve1=Frame(bg="blue",bd="100",height=250,width=250)
cr=Entry(cerceve1)
cr.grid(row=1,column=1)
crChek=Checkbutton(cerceve1,text="Galatasaray")
crChek.grid(row=0,column=1)
cerceve1.grid(row=0,column=1,padx=5,pady=5)

cerceve2=Frame(bg="red",bd="100",height=250,width=250)
crChek1=Checkbutton(cerceve2,text="Avrupa Fatihi")
crChek1.grid(row=1,column=0)
cmb=ttk.Combobox(cerceve2,values=["Muslera","İcardi"])
cmb.grid(row=2,column=0)
cerceve2.grid(row=1,column=0,padx=5,pady=5)

cerceve3=Frame(bg="white",bd="100",height=250,width=250)
c=Checkbutton(cerceve3,text="Ndombili")
c.grid(row=4,column=0)
cerceve3.grid(row=1,column=1,padx=5,pady=5)

pencere.mainloop()