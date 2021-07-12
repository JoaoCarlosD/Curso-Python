class NPC: #Base, Pai, Super
    def __init__(self, nome, time, poder, munição):
        self.nome = nome
        self.time = time
        self.munição = munição
        self.poder = poder
        self.vivo = True
        self.energia = 100
    def info(self):
        print(f"Nome....: {self.nome}")
        print(f"Time....: {self.time}")
        print(f"Poder...: {self.poder}")
        print(f"Munição.: {self.munição}")
        print("Vivo.....: "+("sim" if self.vivo else "não"))
        print(f"Energia..: {self.energia}")
        print("-"*12)
class Soldado(NPC):
    def __init__(self, nome, time, poder, munição):
        self.poder = 200
        self.municao = 90
        super().__init__(nome, time, poder, munição)
class Guarda(NPC):
    def __init__(self, nome, time, poder, munição):
        self.poder = 60
        self.municao = 20
        super().__init__(nome, time, poder, munição)
class Elite(NPC):
    def __init__(self, nome, time, poder, munição):
        self.poder = 400
        self.municao = 180
        super().__init__(nome, time, poder, munição)
    def inf(self):
            super().info()