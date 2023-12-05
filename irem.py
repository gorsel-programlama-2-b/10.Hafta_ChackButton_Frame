# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 14:12:02 2023

@author: C-117
"""

import tkinter as tk


pencere = tk.Tk()


frame1 = tk.Frame(pencere, bg="green")
frame2 = tk.Frame(pencere, bg="blue")
frame3 = tk.Frame(pencere, bg="red")
frame4 = tk.Frame(pencere, bg="white")

frame1.grid(row=0, column=0, padx=10, pady=10)
frame2.grid(row=0, column=1, padx=10, pady=10)
frame3.grid(row=1, column=0, padx=10, pady=10)
frame4.grid(row=1, column=1, padx=10, pady=10)

checbox1 = tk.Checkbutton(frame1, text="checkbutton1")
checbox1.pack(pady=20)

label_frame1 = tk.Label(frame1, text="....")
label_frame1.pack(padx=20, pady=20)

buton_frame1 = tk.Button(frame1, text="Buton 1")
buton_frame1.pack(padx=20, pady=20)

checbox2 = tk.Checkbutton(frame2, text="checkbutton2")
checbox2.pack(pady=20)

label_frame2 = tk.Label(frame2, text="....")
label_frame2.pack(padx=20, pady=20)

entry_frame2 = tk.Entry(frame2)
entry_frame2.pack(padx=20, pady=20)

label_frame3 = tk.Label(frame3, text="....")
label_frame3.pack(padx=20, pady=20)

checbox3 = tk.Checkbutton(frame3, text="checkbutton")
checbox3.pack(pady=10)



checbox4 = tk.Checkbutton(frame4, text="checkbutton4")
checbox4.pack(pady=20)

label_frame4 = tk.Label(frame4, text="....")
label_frame4.pack(padx=20, pady=20)


pencere.mainloop()

