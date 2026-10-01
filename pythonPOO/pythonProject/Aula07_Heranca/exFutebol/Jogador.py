from Pessoa import Pessoa


class Jogador(Pessoa):
    def __init__(self, nome, idade, salario, nmrCamisa, posicao):
        super().__init__(nome, idade, salario)
        self.nmrCamisa = nmrCamisa
        self.posicao = posicao

    def __str__(self):
        return f"Jogador: {self.nome} idade: {self.idade} ganhando R$ {self.salario:.2f} tem a camisa nmr {self.nmrCamisa} e joga na posicao {self.posicao}"

    def jogar_futebol(self):
        print(f"{self.nome} esta em campo")

