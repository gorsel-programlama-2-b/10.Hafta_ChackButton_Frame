from tkinter import*
from tkinter import ttk

sayfa=Tk()

pencere1=Frame(sayfa,bg="green")
pencere1.grid(row=0,column=0,padx=5,pady=5)

chkbtn1 =Checkbutton(pencere1, text="....")
chkbtn1.grid(pady=20)
lbl_eyt =Entry(pencere1)
lbl_eyt.grid(pady=10,padx=10)

pencere2=Frame(sayfa,bg="blue")
pencere2.grid(row=0,column=1,pady=5,padx=5)

chkbtn2 =Checkbutton(pencere2, text=".....")
chkbtn2.grid(pady=20,padx=40)
btn=Button(pencere2,text="Button")
btn.grid(padx=10,pady=10)

pencere3=Frame(sayfa,bg="red")
pencere3.grid(row=1,column=0,padx=5,pady=5)

chkbtn3 =Checkbutton(pencere3, text=".....")
chkbtn3.grid(pady=10)
lbl_cmb=ttk.Combobox(pencere3, values=["yeşil","beyaz","kırmızı","mavi"])
lbl_cmb.grid(padx=10,pady=10)

pencere4=Frame(sayfa,bg="white")
pencere4.grid(row=1,column=1,padx=5,pady=5)

chkbtn4 =Checkbutton(pencere4, text=".....")
chkbtn4.grid(pady=30,padx=40)


sayfa.mainloop()

