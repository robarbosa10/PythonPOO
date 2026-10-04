from abc import ABC
from random import randint


class Personagem(ABC):

    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
        self.mana = 100
        self.dinheiro = 1000
        self.golpes = []

        # Controla se o jogador já atacou nesta rodada
        self.ja_atacou = False

    def atacar(self, alvo):
        # Verifica se o jogador ainda pode atacar
        if self.ja_atacou:
            print("Você já atacou nesta rodada!")
            return
        # Verifica se os jogadores estão vivos
        if self.vida <= 0:
            print(f"{self.nome} está morto e não pode atacar.")
            return
        if alvo.vida <= 0:
            print(f"{alvo.nome} já está derrotado.")
            return
        golpe_aleatorio = randint(1, 7)
        if golpe_aleatorio < 3 and self.mana >= 10:
            print(
                f"VOCÊ CONSEGUIU UM GOLPE LEVE! "
                f"TIROU NO DADO: {golpe_aleatorio}"
            )
            self.mana -= 10
            alvo.vida = max(0, alvo.vida - 10)
        elif golpe_aleatorio <= 6 and self.mana >= 30:
            print(
                f"VOCÊ CONSEGUIU UM GOLPE MODERADO! "
                f"TIROU NO DADO: {golpe_aleatorio}"
            )
            self.mana -= 30
            alvo.vida = max(0, alvo.vida - 30)
        elif golpe_aleatorio == 7 and self.mana >= 50:
            print(
                f"VOCÊ CONSEGUIU UM GOLPE PESADO! "
                f"TIROU NO DADO: {golpe_aleatorio}"
            )
            self.mana -= 50
            alvo.vida = max(0, alvo.vida - 50)
        else:
            print("Você não tem MANA suficiente.")
            print("Golpe ultra-leve!")
            alvo.vida = max(0, alvo.vida - 5)
        self.ja_atacou = True
        if alvo.vida == 0:
            print(f"{alvo.nome} PERDEU!")
        self.mostrar_status(alvo)

    def atributos(self):

        print(f"\n--- * {self.nome} * ---")
        print(f"VIDA = {self.vida}")
        print(f"MANA = {self.mana}")
        print(f"DINHEIRO = R$ {self.dinheiro:.2f}")

    def mostrar_status(self, alvo):

        print("------------------------------------")
        print("JOGADOR 1 - JOGADOR 2")
        print(f"nome = {self.nome} | {alvo.nome}")
        print(f"vida = {self.vida} | {alvo.vida}")
        print(f"mana = {self.mana} | {alvo.mana}")
        print(f"dinheiro = {self.dinheiro} | {alvo.dinheiro}")
        print("------------------------------------")

    def opcoesBatalha(self, alvo):

        while True:

            print("\n====== MENU DE BATALHA ======")

            if self.ja_atacou:
                print("1 = ATACAR (JÁ UTILIZADO)")
            else:
                print("1 = ATACAR")

            print("2 = CURAR")
            print("3 = MANA")
            print("4 = ATRIBUTOS")
            print("5 = PASSAR RODADA")

            try:
                opcao = int(input("Qual a opção? "))
            except ValueError:
                print("Digite apenas números.")
                continue
            if opcao == 1:
                if self.ja_atacou:
                    print("Você já atacou nesta rodada!")
                else:
                    self.atacar(alvo)
            elif opcao == 2:
                self.curar()
            elif opcao == 3:
                self.recuperarMana()
            elif opcao == 4:
                self.atributos()
            elif opcao == 5:
                print(f"{self.nome} passou a rodada.")
                self.ja_atacou = False
                break
            else:
                print("OPÇÃO INVÁLIDA!")
    def curar(self):

        if self.vida >= 100:
            print("Sua VIDA já está em 100%.")
            return

        print(
            "\n1 = ATADURA PEQUENA "
            "(25% DE CURA) - R$ 300\n"
            "2 = ATADURA GRANDE "
            "(50% DE CURA) - R$ 500"
        )

        try:
            opcao = int(input("Qual opção? "))
        except ValueError:
            print("Digite apenas números.")
            return

        if opcao == 1:

            preco = 300
            porcentagem = 0.25
        elif opcao == 2:
            preco = 500
            porcentagem = 0.50
        else:
            print("Opção inválida.")
            return
        if self.dinheiro < preco:
            print("Você não tem dinheiro suficiente.")
            return
        self.dinheiro -= preco
        cura = self.vida * porcentagem
        self.vida = min(100, self.vida + cura)
        print(
            f"Você recuperou {cura:.1f} de VIDA."
        )
        print(
            f"VIDA = {self.vida:.1f} | "
            f"DINHEIRO = R$ {self.dinheiro:.2f}"
        )

    def recuperarMana(self):

        if self.mana >= 100:
            print("Sua MANA já está em 100%.")
            return

        print(
            "\n1 = MANA PEQUENA "
            "(25% DE RECUPERAÇÃO) - R$ 300\n"
            "2 = MANA GRANDE "
            "(50% DE RECUPERAÇÃO) - R$ 500"
        )

        try:
            opcao = int(input("Qual opção? "))
        except ValueError:
            print("Digite apenas números.")
            return

        if opcao == 1:
            preco = 300
            porcentagem = 0.25

        elif opcao == 2:
            preco = 500
            porcentagem = 0.50

        else:

            print("Opção inválida.")
            return

        if self.dinheiro < preco:
            print("Você não tem dinheiro suficiente.")
            return
        self.dinheiro -= preco
        recuperacao = self.mana * porcentagem
        self.mana = min(100, self.mana + recuperacao)
        print(
            f"Você recuperou {recuperacao:.1f} de MANA."
        )
        print(
            f"MANA = {self.mana:.1f} | "
            f"DINHEIRO = R$ {self.dinheiro:.2f}"
        )


class Guerreiro(Personagem):

    def __init__(self, nome):
        super().__init__(nome)

        self.golpes = [
            "ESPADA DO DRAGAO",
            "CHUTE DA SERPENTE"
        ]


class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome)

        self.golpes = [
            "RAIO CONGELANTE",
            "METEORO DE FOGO"
        ]