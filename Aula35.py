from tkinter import *
import os

c = os.path.dirname(__file__)
nomeArquivo = c+"\\nome.txt"
def gravarDados():
    arquivo = open(nomeArquivo,"a")
    arquivo.write(f"Nome....: {vnome.get()}")
    arquivo.write(f"\nTelefone: {vfone.get()}")
    arquivo.write(f"\nEmail...: {vemail.get()}")
    arquivo.write("\nOBS.....:%s" % vobs.get("1.0", END))
    arquivo.close()

app = Tk()
app.title("CFB Cursos")
app.geometry("500x300")
app.configure(background="#dde")
# anchor => N = Norte, S = Sul E = Leste, W = Oeste
# NE = Nordeste, SE = Sudeste, SO = Sudoeste, NO = Noroeste
Label(app,text="Nome",background="#dde",foreground="#009",anchor=W).place(x=10,y=10,width=100,height=20)
vnome = Entry(app)
vnome.place(x=10,y=30,width=200,height=20)

Label(app,text="Telefone",background="#dde",foreground="#009",anchor=W).place(x=10,y=60,width=100,height=20)
vfone = Entry(app)
vfone.place(x=10,y=80,width=100,height=20)

Label(app,text="E-mail",background="#dde",foreground="#009",anchor=W).place(x=10,y=110,width=100,height=20)
vemail = Entry(app)
vemail.place(x=10,y=130,width=300,height=20)

Label(app,text="OBS",background="#dde",foreground="#009",anchor=W).place(x=10,y=160,width=100,height=20)
vobs = Text(app)
vobs.place(x=10,y=180,width=300,height=80)

Button(app,text="Gravar dados",command=gravarDados).place(x=10,y=270,width=100,height=20)
app.mainloop()