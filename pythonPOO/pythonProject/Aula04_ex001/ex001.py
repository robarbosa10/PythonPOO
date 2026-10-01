class MinhaClasse():
    def __init__(self):
        self.nome = "Rogerio"
        self.idade = 30

    def aniversario(self):
        self.idade = self.idade +1
        print(f"{self.nome} fez aniversario, agora ele tem {self.idade} anos")

    def mensagem(self):
        return f"{self.nome} fez {self.idade} anos"


nome = MinhaClasse()

nome.aniversario()

nome.mensagem()