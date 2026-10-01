from Funcionario import Funcioario


class Vendedor(Funcioario):
    def __init__(self, nome, cpf, salario, comissao):
        super().__init__(nome, cpf, salario)
        self.comissao = comissao

    def calcular_comissao(self, valorVenda):
        com = valorVenda * (self.comissao / 100)
        print(f"Valor do salario = {self.salario:.2f} total de vendas R$ {valorVenda:.2f} valor comissao R$ {com:.2f}\n\nVALOR A RECEBER = R$ {self.salario + com:.2f}")