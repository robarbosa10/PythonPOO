from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, sal_bruto):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = 0
        self.sal_minimo = 1612
        self.inss = 7.5


    @abstractmethod
    def calc_salario(self):
        pass


class Horista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trab):
        super().__init__(nome, 0)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calc_salario(self):
        self.sal_bruto = (self.valor_hora * self.horas_trab)
        self.salario = self.sal_bruto - (self.sal_bruto * self.inss /100)
        qtdSalario = self.salario / self.sal_minimo
        print(f"Salario que {self.nome} vai receber é de: R${self.salario:.2f}")
        print(f"Isso equivale a {qtdSalario:.1f} salarios minimo.")

class Mensalista(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
    def calc_salario(self):
        self.salario = self.sal_bruto - (self.sal_bruto * (self.inss / 100))
        qtdSalario = self.salario / self.sal_minimo
        print(f"Salario que {self.nome} vai receber é de: R${self.salario:.2f}")
        print(f"Isso equivale a {qtdSalario:.1f} salarios minimo.")
