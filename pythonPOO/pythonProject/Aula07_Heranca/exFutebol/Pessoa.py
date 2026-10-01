class Pessoa():
    def __init__(self, nome = "", idade = 0, salario = 0):
        self.nome = nome
        self.idade = idade
        self.salario = salario

    def aumentar_salario(self, aumento):
        self.salario += (self.salario * (aumento / 100))
        print(f"seu novo salario é de R$ {self.salario:.2f}")

