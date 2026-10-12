from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, salarioBase):
        self.__nome = nome
        self.__salarioBase = salarioBase

    def getNome(self):
        return self.__nome
    def getSalarioBase(self):
        return self.__salarioBase
    def setNome(self, nome):
        self.__nome = nome
    def setSalarioBase(self, salario):
        self.__salarioBase = salario

    @abstractmethod
    def aprensentar(self):
        pass


class Atendente(Funcionario):
    def __init__(self, nome, salarioBase, atendimentos):
        super().__init__(nome, salarioBase)
        self.__atendimento = atendimentos
    def getAtendimento(self):
        return self.__atendimento
    def setAtendimentos(self, atendimentos):
        if atendimentos > 0:
            self.__atendimento = atendimentos
        else:
            print("Valor errado, nao pode ter menos que 0 atendimentos")

    def calcular_salario(self):
        valor_total = self.getSalarioBase() + (2 * self.getAtendimento())
        print(f"Valor total do salario de {self.getNome()} é de {valor_total:.2f}")

    def aprensentar(self):
        print(f"Nome: {self.getNome()} salario base: {self.getSalarioBase()}")

class Supervisor(Atendente):
    def __init__(self, nome, salarioBase, atendimentos, nomeEquipe ):
        super().__init__(nome, salarioBase, atendimentos)
        self.__nomeEquipe = nomeEquipe

    def getNomeEquipe(self):
        return self.__nomeEquipe

    def setnomeEquipe(self, nome):
        self.__nomeEquipe = nome

    def aprensentar(self):
        print(f"Nome: {self.getNome()} com o salario base de: {self.getSalarioBase()}")
    def calcular_salario(self):
        valor_total = self.getSalarioBase() + (2 * self.getAtendimento()) + 800
        print(f"Valor total do salario de {self.getNome()} (lider da equipe {self.getNomeEquipe()})é de R${valor_total:.2f}")