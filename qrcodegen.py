import qrcode
from tkinter import *
import tkinter.messagebox as msg

t=Tk()

t.geometry("500x500")
t.title("qrcodegen")
t.iconbitmap("qrcode.ico")

def About():
    msg.showinfo("About","Developer name: Hemant Pandey \nVersion:1.0.0 \nThank you for download")

def Exit():
    a=msg.askquestion("Exit","Are you sure you want to exit?")
    if a=="yes":
        msg.showinfo("message","Thank you for use")
        t.quit()
    else:
        pass    

mk=Menu(t)
mymenu=Menu(mk,tearoff=0)
mymenu.add_command(label="about",command=About)
mymenu.add_command(label="Exit",command=Exit)
mk.add_cascade(label="help",menu=mymenu)
t.config(menu=mk)

Label(text="Enter a anything which you want to convert into a qrcode: ").grid(row=0)
var1=StringVar()
Entry(textvariable=var1).grid(row=0,column=1)

Label(text="Enter the name of file: ").grid(row=1)
var2=StringVar()
Entry(textvariable=var2).grid(row=1,column=1)

Label(text="Enter image format(jpg or png): ").grid(row=2)
var3=StringVar()
Entry(textvariable=var3).grid(row=2,column=1)

def submit():
    img=qrcode.make(var1.get())
    if var3.get()=="jpg":
        img.save(var2.get()+".jpg")
    elif var3.get()=="png":
        img.save(var2.get()+".png")
    
Button(text="Submit",command=submit).grid(row=3,column=1)

t.mainloop()