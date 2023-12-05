from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("600x600")

window.rowconfigure((0,1),weight=1,uniform="x")
window.columnconfigure((0,1),weight=1,uniform="x")

positions = [[1,2],[3,4]]
colors = ["red","green","blue","purple"]

def makeWidgets(widget,frame):
    for index,i in enumerate(widget):
        if i == Button:
            i(frame,text="button").grid(row=index,column=0)
        else:
            i(frame).grid(row=index,column=0)

widgets = {
    1:[Checkbutton,Button],
    2:[Checkbutton,Entry],
    3:[Checkbutton,ttk.Combobox],
    4:[Checkbutton]
    }

for row_index,row in enumerate(positions):
    for column_index,cell in enumerate(row):
         frame = Frame(
            window,
            background=colors.pop()
            )
         
         frame.grid(
                row=row_index,
                column=column_index,
                sticky="nswe",
                padx = 5,
                pady = 5
                )
         
         frame.columnconfigure((0),weight=1,uniform="X")
         frame.rowconfigure((0,1),weight=1,uniform="X")     
         makeWidgets(widgets[cell], frame)
        
window.mainloop()
