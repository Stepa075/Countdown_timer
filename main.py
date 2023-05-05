import random
from random import randint
from tkinter import *
from tkinter.messagebox import showerror

root = Tk()


root.title("Countdown timer")
root.geometry('375x117')
root.resizable(False, False)
f1 = LabelFrame(root, text='Число 1')
f2 = LabelFrame(root, text='Знак')
f4 = LabelFrame(root, text='Число 2')
f3 = LabelFrame(root, text='Ответ')
f5 = LabelFrame(root, text='Ответов правильно')
f6 = LabelFrame(root, text='Ответов неправильно')


number1 = Label(f1, text='  1', font=("Arial Bold", 12), width=4)
hours1 = Label(f2, text=' +- ', font=("Arial Bold", 12), width=4)
number2 = Label(f4, text='  2', font=("Arial Bold", 12), width=4)
entry = Entry(f3, font=("Arial Bold", 12), width=7)
hours3 = Label(f5, text=' 0', font=("Arial Bold", 12))
hours4 = Label(f6, text=' 0', font=("Arial Bold", 12))
button1 = Button(f3, text='Ответить', width=10, font=("Arial Bold", 11))  # command=Variables.about
# button1.bind('<Button-1>', control_int)
# entry.bind('<Return>', control_int)

f1.grid(column=0, row=0, sticky=N + S + E + W, padx=2, pady=2)
f2.grid(column=1, row=0, sticky=N + S + E + W, padx=2, pady=2)
f4.grid(column=2, row=0, sticky=N + S + E + W, padx=2, pady=2)
f3.grid(column=3, row=0, sticky=N + S + E + W, padx=2, pady=2)
f5.grid(column=0, columnspan=2, row=2, sticky=N + S + E + W, padx=2, pady=2)
f6.grid(column=2, columnspan=3, row=2, sticky=N + S + E + W, padx=2, pady=2)

number1.grid(column=1, row=0)
hours1.grid(column=1, row=0)
number2.grid(column=1, row=0)
hours3.grid(column=1, row=0)
hours4.grid(column=1, row=0)
entry.grid(column=1, row=0, sticky=N + S + W + E, padx=3, pady=6)
entry.focus()

button1.grid(column=2, row=0, sticky=N + S + W + E, padx=3, pady=6)

# root.after(0, start)
# root.after(0, set_timer)
root.mainloop()
