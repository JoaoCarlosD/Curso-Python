from tkinter import *
from tkinter import ttk

app = Tk()
app.title("Aula 72")
app.geometry("500x475")

def showEsporte():
    print(f"Escolhido: {cb_esportes.get()}")

listEsportes = ["Futebol", "Vôlei", "Basquete"]

lb_Esportes = Label(app, text="Esportes")
lb_Esportes.pack()

cb_esportes = ttk.Combobox(app, values=listEsportes)
cb_esportes.set("Futebol")
cb_esportes.pack()

btn_esporte = Button(app, text="Selecionar", command=showEsporte)
btn_esporte.pack()

app.mainloop()