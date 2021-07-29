import re #RegEx

texto = "Curso de Python do CFB Cursos, canal do youtube"

pesq = input("Pesquisar: ")
res = re.search(pesq,texto)
if res != None:
    pi = res.start()
    pf = res.end()
    tam = pf-pi
    print(f"Começa em {pi}")
    print(f"Termina em {pf}")
    print(tam)
else:
    print("Não encontrado")