#1.
import tkinter
from tkinter import *

root=Tk()

def show():
    print("Hello World")
def terminate():
    exit(0)
root.geometry('250x250')
b1=Button(root,width=20,text='click',command=show)
b1.pack()

b2=Button(root,width=20,text='exit',command=terminate)
b2.pack()

root.mainloop()






#2.
import tkinter
from tkinter import *

root=Tk()

def show():
    var.set("hello world")

def terminate():
    exit(0)

var=StringVar()

root.geometry('250x250')
b1=Button(root,width=20,text='click',command=show)
b1.pack()

b2=Button(root,width=20,text='exit',command=terminate)
b2.pack()

label=Label(root,textvariable=var,width=30)
label.pack()

root.mainloop()








#3.
import tkinter
from tkinter import *

root=Tk()

def show():
    var.set("hello python")

def terminate():
    exit(0)

var=StringVar()

root.geometry('250x250')
b1=Button(root,width=20,text='click',command=show)
b1.pack()

b2=Button(root,width=20,text='exit',command=terminate)
b2.pack()

var.set("hello world")
label=Label(root,textvariable=var,width=30)
label.pack()

root.mainloop()







#4.
import tkinter
from tkinter import *

root=Tk()

def show():
    print(entry.get())
def terminate():
    exit(0)

root.geometry('250x250')

entry=Entry(root,width=30)
entry.pack()

b1=Button(root,width=20,text='click',command=show)
b1.pack()

b2=Button(root,width=20,text='exit',command=terminate)
b2.pack()

root.mainloop()