from tkinter import *
from tkinter import messagebox

app = Tk()
app.title("Aula 64")
app.geometry("500x300")

def showMessage(tipo, msg):
    # askyesno / askquestion - SIM e NÃo (True e False)
    # askokcancel - OK e CANCELAR (True e False)
    # askretrycancel - REPETIR e CANCELAR (True e False)
    # askyesnocancel - SIM, NÃO e CANCELAR (True, False e None)
    if tipo == "info":
        messagebox.showinfo(title="App", message=msg)
    elif tipo == "warning":
        messagebox.showwarning(title="App", message=msg)
    elif tipo == "error":
        messagebox.showerror(title="Error", message=msg)
    else:
        print("Erro")

lista_options = ["info", "warning", "error"]

Label(app, text="Tipo de caixa")
vtipo = StringVar()
vtipo.set("Selecione uma opção")

txtTipos = Label(app, text="Tipos de caixa")
txtTipos.pack()

op_tipos = OptionMenu(app, vtipo, *lista_options).pack()

Label(app, text = "Digite a mensagem").pack()
msg = Entry(app)
msg.pack()

Button(app, text="Criar caixa", command=lambda:showMessage(vtipo.get(), msg.get())).pack()

app.mainloop()