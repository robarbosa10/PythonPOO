from Produto import Produto
class Carrinho:
    def __init__(self):
        self.__produto = []

    def addCarrinho(self, produto):
        self.__produto.append(produto)

    def mostrarCarrinho(self):
        for produto in self.__produto:
            produto.mostrarProduto()
