from tkinter import *

app = Tk()
app.title("CFB Cursos")
app.geometry("500x350")

sb_valores = Spinbox(app,from_=0,to=25)
sb_valores.pack()

app.mainloop()