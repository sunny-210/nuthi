#Tkinter program
from tkinter import *
def display():
    name=e1.get()
    if(name==""):
        val.set("plz Enter Name")
    else:
        val.set("Hello "+name)
    return
window=Tk()
window.geometry("900x300")
val=StringVar()
l1=Label(window,text="Enter the Name",font="times 20")
l1.place(x=50,y=50)
e1=Entry(window,font="times 20")
e1.place(x=250,y=50)
b1=Button(window,text= "Display",font="Times 20", command=display)
b1.place(x=600,y=50)
l2=Label(window,textvariable=val,font="times 30",fg="red")
l2.place(x=100,y=150)
window.mainloop()


