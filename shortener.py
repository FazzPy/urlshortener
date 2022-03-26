import pyshorteners
from tkinter import *

root = Tk()
root.title("URL Kısaltıcı")
root.geometry("300x300+600+230")
root.resizable(width=False, height=False)
root.iconbitmap("url.ico")
backgroundColor = Label(bg="#191970", width=300, height=300)
backgroundColor.place(x=0, y=0)


def kisaltici():
    link = url.get()
    shortener = pyshorteners.Shortener()
    v = shortener.tinyurl.short(link)
    tv = StringVar(value=v)
    sonuc = Entry(width=35, bg="lightgray", fg="black", textvariable=tv)
    sonuc.place(x=100, y=80)

label1 = Label(text="Link Giriniz : ", bg="#191970", fg="white")
label1.place(x=0, y=0)

url = Entry(bg="gray", width=45)
url.place(x=1, y=20)

buton1 = Button(text="Kısalt", command=kisaltici)
buton1.place(x=1, y=45)

label2 = Label(text="Kısaltılmış Link : ", bg="#191970", fg="white")
label2.place(x=0, y=80)

root.mainloop()
