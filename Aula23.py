carros = ["HRV", "Palio", "Jetta", "Fusion"]

itCarros = iter(carros)
while itCarros:
    try:
        print(next(itCarros))
    except StopIteration:
        break