class Funcioario():
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def monstrar_dados(self):
        print("===FUNCIONARIO===")
        print(f"Nome= {self.nome}\nCPF = {self.cpf}\nSalario = {self.salario}")

    def aumentar_salario(self, valorAumento):
        self.salario += (self.salario * (valorAumento / 100))
        print (f"Voce teve um aumento de {valorAumento}% seu novo salario é R$ {self.salario:.2f}")