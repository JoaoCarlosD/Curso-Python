from tkinter import *

def impSenha():
    print(f"Senha digitada: {vsenha.get()}")
app = Tk()
app.title("CFB Cursos")
app.geometry("500x300")

vsenha = StringVar()

p_senha = Entry(app,textvariable=vsenha,show="*")
p_senha.pack()

btn_mostraSenha = Button(app,text="Imprimir senha",command=impSenha)
btn_mostraSenha.pack()

app.mainloop()