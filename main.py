from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.title("Image")
root.geometry("400x400")
upload=Image.open("latte.jpeg")
image=ImageTk.PhotoImage(upload)
label=Label(root,image=image,height=350,width=500)
label.place(x=50,y=50)
label2=Label(root,text="This layered italian icon has made with italian espresso,steamed milk,milk syrup and cream vapour")
label2.place(x=50,y=500)

root.mainloop()