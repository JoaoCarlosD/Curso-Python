import re #RegEx

texto = "Curso de Python do CFB Cursos, canal do youtube"

res = re.sub("\s","_",texto)
print(res)