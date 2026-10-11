from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, modelo, placa, valorDiaria):
        self.__modelo = modelo
        self.__placa = placa
        self.__valorDiaria = valorDiaria

    @abstractmethod
    def informacoes(self):
        pass

    def calcular_valor(self, diaria):
        valor_total = self.getValorDiaria() * diaria
        print(f"Aluguel do {self.getModelo()} por {diaria} dias = R${valor_total:.2f}")
    def getModelo(self):
        return self.__modelo
    def getPlaca(self):
        return self.__placa
    def getValorDiaria(self):
        return  self.__valorDiaria
    def setModelo(self, modelo):
        self.__modelo = modelo
    def setPlaca(self, placa):
        self.__placa = placa
    def setValorDiaria(self, valor):
        self.__valorDiaria = valor
