from tkinter import *
from tkinter import ttk

app = Tk()
app.title("CFB Cursos")
app.geometry("500x350")

listaNomes = [["0", "Bretilda", "99875"], ["1", "Cristina", "2341"], ["2", "Juliana", "99327"]]

tv = ttk.Treeview(app,columns=("id", "nome", "fone"),show= "headings")
tv.column("id",minwidth=0,width=50)
tv.column("nome",minwidth=0,width=250)
tv.column("fone",minwidth=0,width=100)
tv.heading("id",text="ID")
tv.heading("nome",text="NOME")
tv.heading("fone",text="TELEFONE")
tv.pack()
for i,n,f in listaNomes:
    tv.insert("","end",values=(i,n,f))
app.mainloop()