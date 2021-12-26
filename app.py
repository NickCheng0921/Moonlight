import tkinter
from tkinter import messagebox
import crunch

window = tkinter.Tk()
window.title("Python App")
window.geometry("1000x500")
window.resizable(0, 0)


def show_hello():
    crunch.crunch()


myimage = tkinter.PhotoImage(file="sprites/icon.png")

image = tkinter.Label(window, image=myimage, width=500, height=250, )
image.place(x=500, y=400)
image.pack()

space = tkinter.Label(window, height=2, ).pack()

button = tkinter.Button(text=" Generate Chart ", command=show_hello)
button.pack()

window.mainloop()