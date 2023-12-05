from tkinter import *
from tkinter import ttk

window = Tk()
window.tk_setPalette("Blue")
window.geometry("850x850")


frame1 = Frame(bg='lightblue',height=400,width=400,bd=150)
frame1.grid(row=0, column=0,pady=5, padx=5)

frame2 = Frame(bg='lightgreen',height=400,width=400,bd=150)
frame2.grid(row=1, column=0,pady=5, padx=5)

frame3 = Frame(bg='lightpink',height=400,width=400,bd=150)
frame3.grid(row=0, column=1,pady=5, padx=5)

frame4 = Frame(bg='lightyellow',height=400,width=400,bd=150)
frame4.grid(row=1, column=1,pady=5, padx=5)

check1 = Checkbutton(frame1,text ="Test1")
check1.pack()

button1 = Button(frame1,text="test1", bg="white",fg='lightgreen')
button1.pack()

check2 = Checkbutton(frame2, text = "Test 2")
check2.pack()

button2 = Entry(frame2, bg="white")
button2.pack()

check3 = Checkbutton(frame3, text="Test 3")
check3.pack()

button3 = ttk.Combobox(frame3,values=["Test1","Test2","Test3"],background="white")
button3.pack()

check4 = Checkbutton(frame4, text="Test 4")
check4.pack()

button4 = Button(frame4,text="test4", bg="white",fg="red")
button4.pack()


window.mainloop()