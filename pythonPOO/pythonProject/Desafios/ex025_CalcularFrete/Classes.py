from abc import ABC, abstractmethod

class Transportes(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        #self.frete = frete

    @abstractmethod
    def calcular_frete(self):
        pass

class Moto(Transportes):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.distancia = distancia
        self.fator = 0.50

    def calcular_frete(self):
        valorFrete = self.fator * self.distancia
        print(f"valor do frete de MOTO na distancia de {self.distancia}km é: R$ {valorFrete:.2f}")

class Caminhao(Transportes):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 1.20

    def calcular_frete(self):
        if self.distancia < 50:
            print("Distancia nao permitida, tente moto ou drone")
        else:
            valorFrete = self.fator * self.distancia
            print(f"valor do frete de CAMINHÃO na distancia de {self.distancia}km é: R$ {valorFrete:.2f}")


class Drone(Transportes):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 9.50

    def calcular_frete(self):
        if self.distancia > 10:
            print("Nao permitido mandar drone nessa distancia, tente enviar por moto ou caminhao")
        else:
            valorFrete = self.fator * self.distancia
            print(f"valor do frete de DRONE na distancia de {self.distancia}km é: R$ {valorFrete:.2f}")



