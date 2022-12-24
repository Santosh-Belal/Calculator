import pyfiglet

a=pyfiglet.figlet_format("Calculator")

from tkinter import *

import tkinter.messagebox as msgbox

def nefolian():

 msgbox.showinfo("Nefolian","Hello this calculator is \ncreated by Santosh hancy...")

def click(event):

 global screenbar

 text=event.widget.cget("text")

 if text=="=":

   if screenbar.get().isdigit():

    value=int(screenbar.get())

   else:

     try:

      value=eval(screen.get())

    

     except Exception as e:

      print(e)

      value=("Error..")

      screen.update()

   

   screenbar.set(value)

   screen.update()

  

  

 elif text=="C":

  screenbar.set("")

  screen.update()

 else :

  screenbar.set(screenbar.get() + text)

  screen.update()

  

  

root = Tk()

Label(root, text="Calculator",font="Comicsansms 20 bold",bg="blue", borderwidth=3, relief=SUNKEN).pack(fill="x")

screenbar = StringVar()

root.title("Calculator")

screenbar.set("")

screen = Entry(root, textvariable=screenbar,font="lucida 10 bold",bg="red", borderwidth=3, relief=SUNKEN)

screen.pack(pady=20,padx=23,fill=X,ipadx=20)

f= Frame(root,bg="grey")

button=Button(f,text="9",font="Lucida 10 bold",padx=50,pady=40,bg="green",relief=SUNKEN)

button.pack(side=LEFT,padx=20,pady=20)

button.bind("<Button-1>",click)

button=Button(f,text="8",font="Lucida 10 bold",padx=50,pady=40,bg="green",relief=SUNKEN)

button.pack(side=LEFT,padx=20,pady=20)

button.bind("<Button-1>", click)

button=Button(f,text="7",font="Lucida 10 bold",padx=50,pady=40,bg="green",relief=SUNKEN)

button.pack(side=LEFT,padx=20,pady=20)

button.bind("<Button-1>", click)

button=Button(f,text=".",font="Lucida 10 bold",padx=50,pady=40,bg="green",relief=SUNKEN)

button.pack(side=LEFT,padx=26,pady=20)

button.bind("<Button-1>",click)

f.pack()

f= Frame(root,bg="grey")

button=Button(f,text="6",font="Lucida 10 bold",padx=50,pady=40,bg="green",relief=SUNKEN)

button.pack(side=LEFT,padx=22,pady=20)

button.bind("<Button-1>",click)

button=Button(f,text="5",font="Lucida 10 bold",padx=50,pady=40,bg="green",relief=SUNKEN)

button.pack(side=LEFT,padx=24,pady=20)

button.bind("<Button-1>", click)

button=Button(f,text="4",font="Lucida 10 bold",padx=50,pady=40,bg="green",relief=SUNKEN)

button.pack(side=LEFT,padx=23,pady=20)

button.bind("<Button-1>", click)

button=Button(f,text="^",font="Lucida 10 bold",padx=40,pady=40,bg="green",relief=SUNKEN)

button.pack(side=LEFT,padx=23,pady=20)

button.bind("<Button-1>", click)

f.pack()

f= Frame(root,bg="grey")

button=Button(f,text="3",font="Lucida 10 bold",padx=50,pady=40,bg="green",relief=SUNKEN)

button.pack(side=LEFT,padx=19,pady=20)

button.bind("<Button-1>",click)

button=Button(f,text="2",font="Lucida 10 bold",padx=50,pady=40,bg="green",relief=SUNKEN)

button.pack(side=LEFT,padx=19,pady=20)

button.bind("<Button-1>", click)

button=Button(f,text="1",font="Lucida 10 bold",padx=50,pady=40,bg="green",relief=SUNKEN)

button.pack(side=LEFT,padx=19,pady=20)

button.bind("<Button-1>", click)

button=Button(f,text="%",font="Lucida 10 bold",padx=50,pady=40,bg="green",relief=SUNKEN)

button.pack(side=LEFT,padx=19,pady=20)

button.bind("<Button-1>", click)

f.pack()

f= Frame(root,bg="grey")

button=Button(f,text="0",font="Lucida 10 bold",padx=50,pady=40,bg="green",relief=SUNKEN)

button.pack(side=LEFT,padx=22,pady=20)

button.bind("<Button-1>",click)

button=Button(f,text="+",font="Lucida 10 bold",padx=50,pady=40,bg="green",relief=SUNKEN)

button.pack(side=LEFT,padx=21,pady=20)

button.bind("<Button-1>", click)

button=Button(f,text="-",font="Lucida 10 bold",padx=50,pady=40,bg="green",relief=SUNKEN)

button.pack(side=LEFT,padx=22,pady=20)

button.bind("<Button-1>", click)

button=Button(f,text="/",font="Lucida 10 bold",padx=50,pady=40,bg="green",relief=SUNKEN)

button.pack(side=LEFT,padx=22,pady=20)

button.bind("<Button-1>", click)

f.pack()

f= Frame(root,bg="grey")

button=Button(f,text="C",font="Lucida 10 bold",padx=50,pady=40,bg="green",relief=SUNKEN)

button.pack(side=LEFT,padx=26,pady=20)

button.bind("<Button-1>",click)

button=Button(f,text="00",font="Lucida 10 bold",padx=40,pady=40,bg="green",relief=SUNKEN)

button.pack(side=LEFT,padx=16,pady=20)

button.bind("<Button-1>", click)

button=Button(f,text="*",font="Lucida 10 bold",padx=50,pady=40,bg="green",relief=SUNKEN)

button.pack(side=LEFT,padx=16,pady=20)

button.bind("<Button-1>", click)

button=Button(f,text="=",font="Lucida 20 bold",padx=40,pady=40,bg="green",relief=SUNKEN)

button.pack(side=LEFT,padx=21,pady=20)

button.bind("<Button-1>",click)

f.pack()

Button(root, text="Nefolian@gmail.com",font="Comicsansms 14 italic",fg="black",bg="green",padx=20,pady=20, command=nefolian).pack(side=BOTTOM,fill="x")

root.mainloop()

