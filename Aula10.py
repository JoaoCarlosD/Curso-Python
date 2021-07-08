clima = "sol"
dinheiro = 650
lugar = ""
if clima == "sol" or (dinheiro >= 300 and dinheiro <= 500):
    lugar = "clube"
else:
    lugar = "cinema"
print("Vou ao "+lugar)