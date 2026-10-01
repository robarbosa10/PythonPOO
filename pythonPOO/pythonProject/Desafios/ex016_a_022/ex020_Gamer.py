class Gamer():
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos = []

    def addJogos(self, jogo):
        self.jogos.append(jogo)

    def mostrar(self):
        print("-------------------")
        print(f"Nick = {self.nick}")
        print(f"Nome Real = {self.nome}")
        print("-------------------")
        for jogo in self.jogos:
            print(f"jogo = {jogo}")
        print("-------------------")


g1 = Gamer("Rogerio", "Blacktrooper")

g1.addJogos("Fortniete")
g1.addJogos("fifa")

g1.mostrar()

g2 = Gamer("Larissa", "Lari")
g2.addJogos("stardvalley")
g2.addJogos("guitar ghero")


g2.mostrar()