from abc import ABC, abstractmethod
from random import randint, choice

class Personagem(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
        self.mana = 100
        self.dinheiro = 1000
        self.golpes = []
        self.forcaGolpes = [10, 30, 50]

    def atacar(self, alvo):
        if (self.vida > 0 and alvo.vida > 0):
            print("ESCOLHA O SEU GOLPE")
            nmr = 0
            for golpe in self.golpes:
                print(f"{nmr} : {golpe}")
                nmr += 1
                pass


    def atributos(self):
        print(f"---*{self.nome}*---")
        print(f"VIDA = {self.vida}")
        print(f"MANA = {self.mana}")
        print(f"DINHEIRO = R${self.dinheiro}")

    def opcoesBatalha(self, alvo):
        opcao = int(input(
            "1 = ATACAR\n"
            "2 = CURAR\n"
            "3 = MANA\n"
            "4 = ATRIBUTOS\n"
            "5 = PASSAR RODADA\n"
        ))

        while opcao != 5:

            while opcao > 5 or opcao < 1:
                print("OPÇÃO ERRADA, ESCOLHA NOVAMENTE.")
                print(
                    "1 = ATACAR\n"
                    "2 = CURAR\n"
                    "3 = MANA\n"
                    "4 = ATRIBUTOS\n"
                    "5 = PASSAR RODADA"
                )
                opcao = int(input("Qual a opção? "))

            if opcao == 1:
                self.atacar(alvo)

            elif opcao == 2:
                self.curar()

            elif opcao == 3:
                self.recuperarMana()

            elif opcao == 4:
                self.atributos()

            # Pede uma nova opção para a próxima rodada
            opcao = int(input(
                "\n1 = ATACAR\n"
                "2 = CURAR\n"
                "3 = MANA\n"
                "4 = ATRIBUTOS\n"
                "5 = PASSAR RODADA\n"
                "Qual a opção? "
            ))

        DADO = randint(1, 7)

    """def escolha_golpes(self, alvo):
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
            print("JOGO TERMINOU !!!! ")"""
    def curar(self):
        opcao = int(input("1 = ATADURA PEQUENA (25% DE MANA) R$ 300,00\n2 - ATADURA GRANDE (50% MANA) R$ 500,00"))
        while (opcao > 4 or opcao < 0):
            print("opcao errada, tente novamente !")
            opcao = input("1 = ATADURA PEQUENA (25% DE MANA) R$ 300,00\n2 - ATADURA GRANDE (50% MANA) R$ 500,00")
        if (opcao == 1 and self.dinheiro >= 300 and self.vida != 100):
            self.dinheiro = self.dinheiro - 300
            cura = self.vida * (25 / 100)
            if (self.vida + cura > 100):
                self.vida = 100
            else:
                self.vida += cura
            print(f"recebeu {cura}% de cura. SUA VIDA É DE {self.vida}% dinheiro R${self.dinheiro:.2f}")
        elif (opcao == 2 and self.dinheiro > 500 and self.vida != 100):
            self.dinheiro = self.dinheiro - 500
            cura = self.vida * (50 / 100)
            if (self.vida + cura > 100):
                self.vida = 100
            else:
                self.vida += cura
            print(f"recebeu {cura}% de cura. SUA VIDA É DE {self.vida}% dinheiro R${self.dinheiro:.2f}")
        else:
            print("Voce nao tem dinheiro o suficiente ou sua VIDA esta em 100%.")
            pass


    def recuperarMana(self):
        opcao = int(input("1 = MANA PEQUENA (25% DE MANA) R$ 300,00\n2 - MANA GRANDE (50% MANA) R$ 500,00"))
        while (opcao > 4 or opcao < 0):
            print("opcao errada, tente novamente !")
            opcao = input("1 = MANA PEQUENA (25% DE MANA) R$ 300,00\n2 - MANA GRANDE (50% MANA) R$ 500,00")
        if (opcao == 1 and self.dinheiro >= 300 and self.mana != 100):
            self.dinheiro = self.dinheiro - 300
            cura = self.mana * (25 / 100)
            if (self.mana + cura > 100):
                self.mana = 100
            else:
                self.mana += cura
            print(f"recebeu {cura}% de MANA. SUA MANA É DE {self.mana}% dinheiro R${self.dinheiro:.2f}")
        elif (opcao == 1 and self.dinheiro >= 500 and self.mana != 100):
            self.dinheiro = self.dinheiro - 500
            cura = self.mana * (50 / 100)
            if (self.mana + cura > 100):
                self.mana = 100
            else:
                self.mana += cura
            print(f"recebeu {cura}% de cura. SUA VIDA É DE {self.mana}% dinheiro R${self.dinheiro:.2f}")
        else:

            print("Voce nao tem dinheiro o suficiente ou sua MANA está em 100%.")
            pass

    def receber_golpe(self):
        pass

class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.golpes = ["ESPADA DO DRAGAO", "CHUTE DA SERPENTE"]

class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.golpes = ["RAIO CONGELANTE", "METEORO DE FOGO"]

    def recuperarMana(self):
        pass
