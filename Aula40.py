from tkinter import *
from tkinter import messagebox

app = Tk()
app.title("Aula 70")
app.geometry("500x475")

def futebolClicado():
    if futebol.get():
        print("Futebol selecionado!")

def voleiClicado():
    if volei.get():
        print("Vôlei selecionado!")

def basqueteClicado():
    if basquete.get():
        print("Basquete selecionado!")

futebol = IntVar()
volei = IntVar()
basquete = IntVar()

fr_quadro1 = Frame(app, borderwidth = 1, relief="solid")
fr_quadro1.place(x=10, y=10, width=300, height=200)

cb_futebol = Checkbutton(fr_quadro1, text="Futebol", variable=futebol, onvalue=1, offvalue=0, command=futebolClicado)
cb_futebol.pack(side=LEFT)

cb_volei = Checkbutton(fr_quadro1, text="Vôlei", variable=volei, onvalue=1, offvalue=0, command=voleiClicado)
cb_volei.pack(side=LEFT)

cb_basquete = Checkbutton(fr_quadro1, text="Basquete", variable=basquete, onvalue=1, offvalue=0, command=basqueteClicado)
cb_basquete.pack(side=LEFT)

app.mainloop()