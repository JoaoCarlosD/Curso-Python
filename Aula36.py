from tkinter import *

def imprimirEsporte():
    ve = vesporte.get
    print(ve)
    if ve == "f":
        print("Esporte Futebol")
    elif ve == "v":
        print("Esporte Vôlei")
    elif ve == "b":
        print("Esporte Basquete")
    else:
        print("Selecione um esporte")
app = Tk()
app.title("CFB Cursos")
app.geometry("500x300")

vesporte = StringVar() 

bl_esportes = Label(app,text="Esportes")
bl_esportes.pack()

rb_futebol = Radiobutton(app,text="Futebol",value="f",variable=vesporte)
rb_futebol.pack()

rb_volei = Radiobutton(app,text="Vôlei",value="v",variable=vesporte)
rb_volei.pack()

rb_basquete = Radiobutton(app,text="Basquete",value="b",variable=vesporte)
rb_basquete.pack()

btn_esporte = Button(app,text="Esporte selecionado",command=imprimirEsporte)
btn_esporte.pack()

app.mainloop()