class Produto():
    def __init__(self, nome, preco, codigo):
        self.nome = nome
        self.preco = preco
        self.codigo = codigo

    def __str__(self):
        return f"Produto = {self.nome}\nCodigo = {self.codigo}\nCodigo = {self.preco:.2f}"