from abc import ABC, abstractmethod

class Personagem(ABC):
    def __init__(self, nome, vida, golpes):
        self.nome = nome
        self.vida = vida
        self.golpes = golpes

    def atacar(self, alvo, forca):
        pass

    def receber_dano(self, dano):
        pass

    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):

    def curar(self):
        pass

class Mago(Personagem):
    pass
