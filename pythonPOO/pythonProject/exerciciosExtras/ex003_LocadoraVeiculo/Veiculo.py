from Locadora import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo, placa, valorDiaria, portas):
        super().__init__(modelo, placa, valorDiaria)
        self.__portas = portas

    def getPortas(self):
        return self.__portas
    def setPortas(self, portas):
        self.__portas = portas

    def informacoes(self):
        print(f"Modelo = {self.getModelo()} - PLACA = {self.getPlaca()} - "
              f"VALOR DIARIA = {self.getValorDiaria()} - PORTAS = {self.getPortas()}")

class Moto(Veiculo):
    def __init__(self, modelo, placa, valorDiaria, cilindrada):
        super().__init__(modelo, placa, valorDiaria)
        self.__cilindrada = cilindrada

    def getCilindradas(self):
        return self.__cilindrada
    def setCilindradas(self, cilindradas):
        self.__cilindrada = cilindradas


    def informacoes(self):
        print(f"Modelo = {self.getModelo()} - PLACA = {self.getPlaca()} - "
              f"VALOR DIARIA = {self.getValorDiaria()} - CILINDRADAS = {self.getCilindradas()}")
