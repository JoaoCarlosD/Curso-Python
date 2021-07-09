import os
from time import sleep
carros = []
carro = input("Digite o nome do novo carro: ")
while carro != "-1":
    carros.append(carro)
    carro = input("Digite o nome do novo carro: ")
os.system("cls")
for x in carros:
    print(x)
print("\nFim do loop")
sleep(10) #Para o programa pelo tempo determinado