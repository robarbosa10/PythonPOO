from os import getenv

from Carrinho import Carrinho

class Produto:
    def __init__(self, nome, preco, estoque):
        self.__nome = nome
        self.__preco = preco
        self.__estoque = estoque
        self.__addCarrinho = 0

    def getAddCarrinho(self):
        return self.__addCarrinho
    def setAddCarrinho(self, add):
        self.__addCarrinho = add

    def getNome(self):
        return self.__nome
    def getPreco(self):
        return self.__preco
    def getEstoque(self):
        return self.__estoque
    def setNome(self, nome):
        self.__nome = nome
    def setPreco(self, preco):
        if(preco < 0):
            print("Erro, valor invalido")
        else:
            self.__preco = preco
    def setEstoque(self, estoque):
        if(estoque < 0):
            print("Estoque invalido")
        else:
            self.__estoque = estoque

    def retirar_estoque(self, qtd):
        if(self.getEstoque() >= qtd):
            self.setAddCarrinho(qtd)
            self.setEstoque(self.getEstoque() - qtd)



