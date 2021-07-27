import os

carros = []

class Carro:
    nome = ""
    pot = 0 #horsepower
    velMax = 0 #km
    ligado = False
    def __init__(self, nome, pot):
        self.nome = nome
        self.pot = pot
        self.velMax = pot*2
    def ligar(self):
        self.ligado = True
    def desligar(self):
        self.ligado = False
    def info(self):
        print(f"Nome.......: {self.nome}")
        print(f"Potência...: {self.pot}")
        print(f"Vel.Máxima.: {self.velMax}")
        print("Ligado.....: "+("sim" if self.ligado == True else "não"))
def Menu():
    os.system("cls") or None
    print("[ 1 ] Novo Carro")
    print("[ 2 ] Informações do Carro")
    print("[ 3 ] Excluir Carro")
    print("[ 4 ] Ligar Carro")
    print("[ 5 ] Desligar Carro")
    print("[ 6 ] Listar Carro")
    print("[ 7 ] Sair")
    print("Quantidade de carros "+str(len(carros)))
    opc = input("Digite sua opção: ")
    return opc
def NovoCarro():
        os.system("cls")
        n = str(input("Nome do Carro.....: "))
        p = int(input("Potência do Carro.: "))
        car = Carro(n,p)
        carros.append(car)
        print("Novo carro criado!")
        os.system("pause")
def informações():
    os.system("cls")
    n = input("Informe o número do carro que deseja ver as informações: ")
    try:
        carros[int(n)].info()
    except:
        print("Carro não existe na lista")
    os.system("pause")
def excluirCarro():
    os.system("cls")
    n = int(input("Informe o número do carro que deseja excluir: "))
    try:
        carros[int(n)]
    except:
        print("Carro não existe na lista!")
        os.system("pause")
def ligarCarro():
    os.system("cls")
    n = int(input("Informe o número do carro que deseja ligar: "))
    try:
        carros[int(n)].ligar()
        print("Carro ligado!")
    except:
        print("Carro não existe na lista!")
    os.system("pause")
def desligarCarro():
    os.system("cls")
    n = int(input("Informe o número do carro que deseja ligar: "))
    try:
        carros[int(n)].desligar()
        print("Carro desligado!")
    except:
        print("Carro não existe na lista!")
    os.system("pause")
def listarCarros():
    os.system("cls")
    p = 0
    for c in carros:
        print(f"{p} - {c.nome}")
        p += 1
    os.system("pause")
ret = Menu()
while ret < "7":
    if ret == "1":
        NovoCarro()
    elif ret == "2":
        informações()
    elif ret == "3":
        excluirCarro()
    elif ret == "4":
        ligarCarro()
    elif ret == "5":
        desligarCarro()
    elif ret == "6":
        listarCarros()
    ret = Menu()
os.system("cls") or None
print("Programa Finalizado")