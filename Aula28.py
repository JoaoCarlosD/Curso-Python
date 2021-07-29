import re #RegEx

texto = "Curso de Python do CFB Cursos, canal do youtube"

pesq = input("Pesquisar: ")
res = re.findall(pesq,texto)
print(res)
qtd = len(res)
print(f"Quantidade: {qtd}")
for t in res:
    print(t)