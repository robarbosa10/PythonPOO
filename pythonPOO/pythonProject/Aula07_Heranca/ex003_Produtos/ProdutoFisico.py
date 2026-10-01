from Produto import Produto

class ProdutoFisico(Produto):
    def __init__(self, nome, preco, codigo, peso, estoque):
        super().__init__(nome, preco, codigo)
        self.peso = peso
        self.estoque = estoque
        """self.altura = 0
        self.largura = 0
        self.comprimento = 0"""

    def calcular_frete(self):
        precoFrete = self.peso * 10
        print(f"Valor do frete é {precoFrete:.2f}")

    def mostrar_produto(self):
        print("====PRODUTO====")
        print(f"{self.nome}")
        print(f"Codigo = {self.codigo}")
        print(f"Preco = {self.preco:.2f}")
        print(f"PESO = {self.peso:.2f}")
        print(f"ESTOQOUE = {self.estoque}")