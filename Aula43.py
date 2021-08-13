from tkinter import *
from tkinter import ttk

app = Tk()
app.title("CFB Cursos")
app.geometry("500x350")

lb_valor = Label(app,text="Valor")
lb_valor.pack()

sc_escala = Scale(app,from_=0,to=100,orient=HORIZONTAL)
sc_escala.set(25)
sc_escala.pack()

def valorEscala():
    print(f"Valor da escala: {sc_escala.get()}")
    
app.mainloop()