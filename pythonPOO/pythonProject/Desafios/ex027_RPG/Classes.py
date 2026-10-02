from abc import ABC, abstractmethod
from random import randint, choice

class Personagem(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
        self.mana = 100
        self.golpes = []

    def atacar(self, alvo):
        self.escolha_golpes(alvo)

    def escolha_golpes(self, alvo):
        if(self.vida > 0 and alvo.vida > 0):
            print("ESCOLHA O SEU GOLPE")
            nmr = 0
            for golpe in self.golpes:
                print(f"{nmr} : {golpe}")
                nmr += 1
            opcao= int(input("Qual o numero do golpe? "))
            DADO = randint(1, 7)

            if(DADO < 3):
                print(f"Golpe = {self.golpes[opcao]}")
                print(f"Dado caiu no numero {DADO} dano BAIXO")
                print(f"*-*-*-*-*-*-*--*-*--*-*-*-*-*-*")
                forca_golpe = 10
                if forca_golpe <= self.mana:
                    self.mana = self.mana - 10
                    alvo.vida -= forca_golpe
                else:
                    print("Erro, voce nao tem mais MANA")
                    pass
            elif(DADO >= 3 and DADO <=6):
                print(f"Golpe = {self.golpes[opcao]}")
                print(f"Dado caiu no numero {DADO} dano MODERADO")
                print(f"*-*-*-*-*-*-*--*-*--*-*-*-*-*-*")
                forca_golpe = 30
                if forca_golpe <= self.mana:
                    self.mana = self.mana - 30
                    alvo.vida -= forca_golpe
                else:
                    print("Erro, voce nao tem mais MANA")
                    pass
            elif(DADO == 7):
                print(f"Golpe = {self.golpes[opcao]}")
                print(f"Dado caiu no numero {DADO} dano PESADO")
                print(f"*-*-*-*-*-*-*--*-*--*-*-*-*-*-*")
                forca_golpe = 50
                if forca_golpe <= self.mana:
                    self.mana = self.mana - 50
                    alvo.vida -= forca_golpe
                else:
                    print("Erro, voce nao tem mais MANA")
                    pass
            print(f"***** {self.nome} atacou {alvo.nome} *****")
            print(f"VIDA DE {self.nome}: {self.vida}")
            print(f"VIDA DE {alvo.nome}: {alvo.vida}")
            print(f"MANA DE {self.nome}: {self.mana}")
            print(f"MANA DE {alvo.nome}: {alvo.mana}")
        else:
            print("JOGO TERMINOU !!!! ")

    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.golpes = ["ESPADA DO DRAGAO", "CHUTE DA SERPENTE"]



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
        self.golpes = ["RAIO CONGELANTE", "METEORO DE FOGO"]



    def curar(self):
        cura = randint(1, 100)
        if (self.vida + cura > 100):
            self.vida = 100
        else:
            self.vida += cura
        print(f"{self.nome} usou magia de cura e recebeu {cura} pontos de vida e agora tem {self.vida} ")
