import tkinter
from tkinter.constants import X, Y
from typing import Text

app = tkinter.Tk()
app.title("CFB Cursos")
app.geometry("500x300")
app.configure(background="#008")

txt1 = tkinter.Label(app,text="Curso de Python",background="#ff0",foreground="#000")
txt1.place(x=10,y=10,width=150,height=30)
vtxt = "Módulo Tkinter"
vbg = "#ff0"
vfg = "#fff"
txt2 = tkinter.Label(app,text=vtxt,bg=vbg,fg=vfg)
txt2.pack(ipadx=20,ipady=20,padx=5,pady=5,side="top",fill=Y,expand=True)
app.mainloop()