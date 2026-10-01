from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass
    @abstractmethod
    def area(self):
        pass


class Quadradro(Poligono):
    def __init__(self, lado, qtd_lados):
        super().__init__(qtd_lados)
        self.lado = lado

    def perimetro(self):
        pass

    def area(self):
        pass

class Circulo(Poligono):
    def __init__(self, raio, qtd_lados):
        super().__init__(qtd_lados)
        self.radio = raio

    def perimetro(self):
        pass
    def area(self):
        pass