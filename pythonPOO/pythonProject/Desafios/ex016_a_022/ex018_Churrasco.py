class Churrasco():
    def __init__(self, titulo,qtdPessoas = 100):
        self.qtdPessoas = qtdPessoas
        self.titulo = titulo
        self.qtdCarne = 0.400
        self.valorKg = 82.40

    def analisar(self):
        qtdComprar = self.qtdPessoas * self.qtdCarne
        qtdTotal = qtdComprar * self.valorKg
        valorPessoa = (self.valorKg * qtdComprar) / self.qtdPessoas

        print(f"Quantidade de convidados {self.qtdPessoas} recomento comprar {qtdComprar:.4f}kg  valor total R$ {qtdTotal:.2f} valor por pessoa: R$ {valorPessoa:.2f}")

churras = Churrasco("Curras")


churras.analisar()