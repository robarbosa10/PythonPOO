class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        print("------------Produto------------")
        print(f"|         {self.nome}        |")
        print("|-----------------------------|")
        print(f"|       R${self.preco}       |")
        print("-------------------------------")


p1 = Produto("Celular", 1250.00)
p2 = Produto("Notebook", 2350.00)

p1.etiqueta()
p2.etiqueta()