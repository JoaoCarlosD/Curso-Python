import os
import re
import os

nome = "TesteAula32"
caminho = "C:/Users/Administrador/Desktop/Curso-Python/"
if os.path.exists(caminho+nome):
    print("Arquivo existente")
else:
    global f
    f = open(caminho+nome,"x")
    f.close()
    print("Arquivo criado")
if os.path.exists(caminho+nome):
    os.remove(caminho+nome)
    print("Arquivo removido")
else:
    print("Arquivo inexistente")
# r = read
# a = append - anexar
# w = write
# x = create