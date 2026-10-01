from Funcionario import Funcioario


class Desenvolvedor(Funcioario):
    def __init__(self, nome, cpf, salario, linguagemProg):
        super().__init__(nome, cpf, salario)
        self.linguagemProg = linguagemProg

    def mostrar_dados(self):
        print(f"Nome = {self.nome}\nCPF = {self.cpf}\nSalario = R$ {self.salario:.2f}\nLinguagem principal = {self.linghagemProg}")