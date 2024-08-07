from tkinter import*
from tkinter import filedialog
import tkinter as tk
import PIL
from PIL import ImageTk
from PIL import Image
import os
from stegano import lsb

root = Tk()
root.title("Steganography - Hide a Secret Text Message in an Image")
root.geometry("700x500+250+180")
root.resizable(False,False)
root.configure(bg="#2f4155")

def showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(), title='Chouse Image', filetype=(("PNG file","*.png"), ("JPG file","*.jpg"), ("All files","*.txt")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=250,height=250)
    lbl.image=img

def hidedata():
    global secret
    secret_message=text1.get(1.0,END)
    secret = lsb.hide(str(filename), secret_message)

def saveimage():
    secret.save("hidden.png")

def showdata():
    clear_messages = lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_messages)

#icon
image_icon=PhotoImage(file="logo.jpg")
root.iconphoto(False,image_icon)

#logo
logo=PhotoImage(file="logo.png")
Label(root,image=logo,bg="#2f4155").place(x=10,y=0)
Label(root,text="Crytography",bg="#2d4155",fg="white",font="arial 25 bold").place(x=100,y=20)

#First Frame
f1=Frame(root,bd=3,bg="black",width=340,height=280,relief=GROOVE)
f1.place(x=10,y=80)

lbl=Label(f1,bg="black")
lbl.place(x=40,y=10)

#Second Frame
f2=Frame(root,bd=3,bg="white",width=340,height=280,relief=GROOVE)
f2.place(x=350,y=80)

text1=Text(f2,font="Robote 20",bg="white",fg="black",relief=GROOVE)
text1.place(x=0,y=0,width=320,height=295)

scrollbar1=Scrollbar(f2)
scrollbar1.place(x=320,y=0,height=300)
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#Third Frame
f3=Frame(root,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
f3.place(x=10,y=370)

Button(f3,text="Open Image",width=10,height=2,font="arial 14 bold",command=showimage).place(x=20,y=30)
Button(f3,text="Save Image",width=10,height=2,font="arial 14 bold",command=saveimage).place(x=180,y=30)
Label(f3,text="Image, Pics, All Files", bg="#2f4155",fg="yellow").place(x=20,y=5)

#Fourth Frame
f4=Frame(root,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
f4.place(x=360,y=370)

Button(f4,text="Hide Data",width=10,height=2,font="arial 14 bold",command=hidedata).place(x=20,y=30)
Button(f4,text="Show Data",width=10,height=2,font="arial 14 bold",command=showdata).place(x=180,y=30)
Label(f4,text="Steganography", bg="#2f4155",fg="yellow").place(x=20,y=5)

root.mainloop()
