from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    def preparar(self):
        print("--INICIANDO PREPARO--")
        self.ferver_agua()
        self.misturar()
        self.servir()
        print(" --- BEBIDA PRONTA ---")

    def ferver_agua(self):
        print(f"1: Fervendo agua a 100 graus Celcius")

    @abstractmethod
    def misturar(self):
        pass
    def servir(self):
        pass


class Cafe(BebidaQuente):
    def misturar(self):
        print(f"2: Passando a agua quente pelo pó do café moido")
    def servir(self):
        print("3: Servindo cafe numa xicara pequena")

class Leite(BebidaQuente):
    def misturar(self):
        print("2: Passandro vapor pressurizado pelo bico do leite")
    def servir(self):
        print("3: Servindo na caneca grande ja com café.")

class Cha(BebidaQuente):
    def misturar(self):
        print("2: Mergulhando o sachê de ervas na agua.")
    def servir(self):
        print("3: Servindo na caneca de porcelana com limão")

