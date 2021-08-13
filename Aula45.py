from tkinter import *

app = Tk()
app.title("CFB Cursos")
app.geometry("500x350")

listaEsportes = ["Futebol", "Vôlei", "Basquete"]

lb_esportes = Listbox(app)
for esportes in listaEsportes:
    lb_esportes.insert(END,esportes)
lb_esportes.pack()

def imprimirEsporte():
    print(f"Esporte: {lb_esportes.get(ACTIVE)}")
def addEsporte():
    lb_esportes.insert(END,vnovoesporte.get())
btn_esporte = Button(app, text="Selecionar", command=imprimirEsporte)
btn_esporte.pack()
vnovoesporte = Entry(app)
vnovoesporte.pack()
btn_inserirEsporte = Button(app, text="Adicionar esporte", command=addEsporte)
btn_inserirEsporte.pack()

app.mainloop()