from tkinter import *
from tkinter import ttk
from typing import TextIO
app = Tk()
app.title("CFB Cursos")
app.geometry("500x350")

nb = ttk.Notebook(app)
nb.place(x=0,y=0,width=500,height=300)

tb1 = Frame(nb)
nb.add(tb1,text="Cursos")

tb2 = Frame(nb)
nb.add(tb2,text="Canal")

lb1 = Label(tb1,text="Curso de Python")
lb1.pack()
lb2 = Label(tb2,text="CFB Cursos")
lb2.pack()

app.mainloop()