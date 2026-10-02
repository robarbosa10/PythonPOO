from abc import ABC, abstractmethod
from random import randint, choice

class Personagem(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
        self.mana = 100
        self.golpes = []

    def atacar(self, alvo, forca):
        if(self.vida > 0 and alvo.vida > 0):
            alvo.vida = alvo.vida - forca
            self.mana = self.mana - forca
            print(f"---{self.nome}---\nVIDA = {self.vida}\nMANA = {self.mana}\n atacou {alvo.nome} e agora tem vida de {alvo.vida}")
            print(f"{self.nome} atacou {alvo.nome} e agora tem vida de {alvo.vida}")

    def receber_ataque(self):
        pass

    def escolha_golpes(self, alvo):
        print("ESCOLHA O SEU GOLPE")
        nmr = 0
        for golpe in self.golpes:
            print(f"{nmr} : {golpe}")
            nmr += 1
        opcao= int(input("Qual o numero do golpe? "))
        DADO = randint(1, 7)
        if(DADO < 3):
            print(f"Golpe = {self.golpes[opcao]} dado caiu no numero {DADO} dano leve")
            forca_golpe = 10
            self.mana = self.mana - 5
            alvo.vida -= forca_golpe
        elif(DADO >= 3 and DADO <=6):
            print(f"Golpe = {self.golpes[opcao]} dado caiu no numero {DADO} dano moderado")
            forca_golpe = 30
            self.mana = self.mana - 20
            alvo.vida -= forca_golpe
        elif(DADO == 7):
            print(f"Golpe = {self.golpes[opcao]} dado caiu no numero {DADO} dano PESADO")
            forca_golpe = 50
            self.mana = self.mana - 50
            alvo.vida -= forca_golpe
        print(f"*****{self.nome} | {alvo.nome}")
        print(f"VIDA = {self.vida} | {alvo.vida}")
        print(f"MANA = {self.mana} |{alvo.mana}")

    def receber_dano(self, dano):
        pass

    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.golpes = ["espada de dragao", "chute da serpente"]



    def curar(self):
        cura = randint(1, 100)
        if(self.vida + cura > 100):
            self.vida = 100
        else:
            self.vida += cura
        print(f"{self.nome} usou ataduras e recebeu {cura} pontos de vida e agora tem {self.vida} ")
class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.golpes = ["raio congelante", "meteoro de pegasus"]



    def curar(self):
        cura = randint(1, 100)
        if (self.vida + cura > 100):
            self.vida = 100
        else:
            self.vida += cura
        print(f"{self.nome} usou magia de cura e recebeu {cura} pontos de vida e agora tem {self.vida} ")
