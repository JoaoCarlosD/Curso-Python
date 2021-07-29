import re #RegEx

texto = "Curso de Python do CFB Cursos, canal do youtube"

res = re.split("d",texto)

for t in res:
    print(t)