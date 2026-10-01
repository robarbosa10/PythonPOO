class MinhaClasse():
    def __init__(self, n = "", i = 0):
        self.nome = n
        self.idade = i

    def aniversario(self):
        self.idade = self.idade +1
        print(f"{self.nome} fez aniversario, agora ele tem {self.idade} anos")

    def __str__(self):
        return f"{self.nome} fez {self.idade} anos"


p1 = MinhaClasse("Maria", 17)
p2 = MinhaClasse("Rogerio", 30)

p1.aniversario()
p2.aniversario()

print(p2)