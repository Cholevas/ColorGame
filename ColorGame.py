from tkinter import *
from tkinter import messagebox
import random

win = Tk()
win.title("Color Game")
win.geometry("300x300")


timeleft = 45

x=0

ruleslbl = Label(win, text="Try to guess the color of the text!")
ruleslbl.grid(column=1, row=1)
lbl = Label(win, text = "Press Enter to Start!")
lbl.grid(column = 1, row = 2)
timelbl = Label (win, text = "Time Left: " + str(timeleft))
timelbl.grid(column = 1, row = 3)

colorlbl = Label(win,font = ("Times",50), text = "color")
colorlbl.grid(column= 1, row = 4)

txt = Entry(width= 30)
txt.grid(column = 1, row = 5)

pointslbl = Label(win,text =str(x))
pointslbl.grid(column = 1, row= 6)




colors = ["red", "blue", "black", "cyan", "yellow", "orange", "purple", "brown", "pink", "lime"]

def countdown():
    global timeleft
    global x
    timeleft = int(timeleft) - 1
    if (timeleft < 1):
        win.destroy()
        messagebox.showinfo("SCORE","Your final score was: " + str(x))


    timelbl.config(text ="Time Left: " + str(timeleft))
    Start()

def Start(*args):
    timelbl.after(1000, countdown)
    win.bind("<space>", colorshuffle)


def colorshuffle(*args):
    global x
    global text
    text = txt.get()
    text=text[: -1]
    if text == str(colors[1]):
        x = x + 1
        pointslbl.config(text = str(x))
    txt.delete(0, 'end')
    random.shuffle(colors)
    colorlbl.config(fg=str(colors[1]),text = str(colors[0]))



win.bind("<Return>", Start)

win.mainloop()