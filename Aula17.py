from random import randint
contErros = 0
sorteado = randint(0,100)
jogador = int(input("Digite um número entre 0 e 100: "))
while sorteado != jogador:
    if sorteado > jogador:
        print("ERRO, o número é maior")
    elif sorteado < jogador:
        print("ERRO, o número é menor")
    contErros += 1
    jogador = int(input("Digite seu número: "))
print(f"Número {jogador}, você acertou em {contErros} tentativas")