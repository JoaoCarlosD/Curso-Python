from time import sleep
valores = [1, 3, 5, 2]
def somar(num):
    r = 0
    for n in num:
        r += n
    return r
r = somar(valores)
print(f"{valores} : Soma = {somar(valores)}")
sleep(20)