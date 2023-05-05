import datetime
from tkinter import *
from time import sleep


def setwindow(root_main):
    root_main.title("Countdown timer")
    root_main.resizable(False, False)

    w = 350
    h = 200
    ws = root_main.winfo_screenwidth()
    wh = root_main.winfo_screenheight()

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)

    root_main.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))


root_main = Tk()
setwindow(root_main)
frame = Frame(master=root_main, bg="#3333ff")
frame.pack(fill=BOTH, expand=True)

# root_main.bind("<Return>", podschet)
# root_main.bind("<Up>", "")
# root_main.bind("<Down>", "")

root_main.mainloop()
