from tkinter import *
import os

app = Tk()
app.title("CFB Cursos")
app.geometry("500x300")
app.configure(background="#dde")

def semComando():
    print("Comando será adicionado em breve")

barradeMenus = Menu(app)
menuContatos = Menu(barradeMenus,tearoff=0)
menuContatos.add_command(label="Novo",command=semComando)
menuContatos.add_command(label="Pesquisar",command=semComando)
menuContatos.add_command(label="Deletar",command=semComando)
menuContatos.add_separator()
menuContatos.add_command(label="Fechar",command=app.quit)
menuContatos.add_cascade(label="Contatos",command=menuContatos)

menuManutencao = Menu(barradeMenus,tearoff=0)
menuManutencao.add_command(label="Banco de dados",command=semComando)
menuSobre = Menu(barradeMenus,tearoff=0)
menuSobre.add_command(label="CFB Cursos",command=semComando)
barradeMenus.add_cascade(label="Sobre",menu = menuSobre)
app.config(menu=barradeMenus)
app.mainloop()