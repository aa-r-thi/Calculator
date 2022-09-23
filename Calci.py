from distutils.cmd import Command
from tkinter import *
from tokenize import Floatnumber

root = Tk()

input = Entry(root,width=50,bg="pink",fg="black")
input.grid(row=0,column=0,padx=10,pady=10,ipadx=10,ipady=10,columnspan=3)

def click(num):
    comment = input.get()
    input.delete(0,END)
    input.insert(0,str(comment)+str(num))
    return 

def add():
    comment = input.get()
    global fnum 
    fnum = int(comment)
    input.delete(0,END)
    return

def acc():
    input.delete(0,END)
    return

def equal():
    comment = input.get()
    snum = int(comment)
    input.delete(0,END)
    input.insert(0,fnum+snum)
    return

button1 = Button(root,text="1",padx=50,pady=25,bg="blue",command=lambda: click(1))
button2 = Button(root,text="2",padx=50,pady=25,bg="blue",command=lambda: click(2))
button3 = Button(root,text="3",padx=50,pady=25,bg="blue",command=lambda: click(3))
button4 = Button(root,text="4",padx=50,pady=25,bg="blue",command=lambda: click(4))
button5 = Button(root,text="5",padx=50,pady=25,bg="blue",command=lambda: click(5))
button6 = Button(root,text="6",padx=50,pady=25,bg="blue",command=lambda: click(6))
button7 = Button(root,text="7",padx=50,pady=25,bg="blue",command=lambda: click(7))
button8 = Button(root,text="8",padx=50,pady=25,bg="blue",command=lambda: click(8))
button9 = Button(root,text="9",padx=50,pady=25,bg="blue",command=lambda: click(9))
button0 = Button(root,text="0",padx=50,pady=25,bg="blue",command=lambda: click(0))


button_add = Button(root,text="+",padx=106.5,pady=25,bg="blue",command=add)
button_ac = Button(root,text="AC",padx=45,pady=25,bg="blue",command=acc)
button_equal = Button(root,text="=",padx=106.5,pady=25,bg="blue",command=equal)


button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button0.grid(row=4,column=0)
button_add.grid(row=4,column=1,columnspan=2)
button_ac.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)


root = mainloop()