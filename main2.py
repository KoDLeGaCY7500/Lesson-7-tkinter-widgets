from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("400x400")
def msg():
    messagebox.showwarning("Alert","Stop! Virus has been detected on this file. Are you sure you want to continue?")
button=Button(root,text="Install your special credits",command=msg)
button.place(x=45,y=40)


root.mainloop()