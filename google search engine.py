from tkinter import *
from tkinter import font
from tkinter import Label
import webbrowser
from PIL import ImageTk,Image
import googlesearch

root=Tk()
root.title("google search engine")
root.resizable(0,0)
root.geometry("800x500")
root.configure(bg="#C0C0C0")

#action fun code starts 
def callback(url):
   webbrowser.open(url)

#label create
l1=Label(root,bg="black",width=500,height=2)
l1.grid(sticky="w")

#app logo
apps_logo=ImageTk.PhotoImage(Image.open("ggl.png"))
a=Label(root,image=apps_logo,borderwidth=0)
a.place(x=0,y=3)

#apps label
apps=Label(root,text="apps",bg="black",fg="white")
apps.place(x=30,y=3)
apps.bind("<Button-1>",lambda e :callback("www.google.com"))

#youtube image
yt_logo=ImageTk.PhotoImage(Image.open("you33.png"))
y=Label(root,image=yt_logo,borderwidth=0)
y.place(x=70,y=8)

#youtube Label
yt=Label(root,text="youtube",bg="black",fg="white")
yt.place(x=110,y=3)
yt.bind("<Button-1>",lambda e :callback("https://www.youtube.com/"))

#google drive image
# gd_logo=ImageTk.PhotoImage(Image.open("gdrive1.png"))
# d=Label(root,image=gd_logo,borderwidth=0)
# d.place(x=170,y=3)


# #gmail image
gm_logo=ImageTk.PhotoImage(Image.open("gmail31.png"))
g=Label(root,image=gm_logo,borderwidth=0)
g.place(x=170,y=3)

#gmail label
drive=Label(root,text="gmail",bg="black",fg="white")
drive.place(x=220,y=3)
drive.bind("<Button-1>",lambda e :callback("https://mail.google.com/mail/"))

#google drive label
drive=Label(root,text="googledrive",bg="black",fg="white")
drive.place(x=270,y=3)
drive.bind("<Button-1>",lambda e :callback("https://drive.google.com/"))

#only gmail label
g=Label(root,text="gmail",cursor="hand2")
g.place(x=630,y=50)
g.bind("<Button-1>",lambda e :callback("https://mail.google.com/mail/"))

#google image
g_logo=ImageTk.PhotoImage(Image.open("gogle.png"))
l2=Label(root,image=g_logo)
l2.place(x=100,y=120)

def search():
    url=(f"www.google.com/search?q={entry.get()}")
    #url=entry.get()
    webbrowser.open(url)

entry=Entry(root,width=90)
entry.place(x=150,y=370)

button=Button(root,text="search",command=search)
button.place(x=450,y=400)

root.mainloop()
