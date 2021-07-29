import json

with open('C:/Users/Administrador/Desktop/Curso-Python/Aula27.json') as f:
    jogador = json.load(f)

def separador():
    print("-"*50)
for c in jogador:
    print(c)
separador()
for i in jogador.items():
    print(i)
separador()
for v in jogador.values():
    print(v)