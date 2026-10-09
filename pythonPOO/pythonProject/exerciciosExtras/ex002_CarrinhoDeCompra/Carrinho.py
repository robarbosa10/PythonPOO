#from Produto import Produto


class Carrinho:
    def __init__(self):
        self.__produto = []

    def addCarrinho(self, produto, qtd):
        produto.retirar_estoque(qtd)
        self.__produto.append(produto)
        self.mostrarCarrinho(qtd)



    def mostrarCarrinho(self, qtd):
        n = 1
        for produto in self.__produto:
            valor_total = valor_total + (produto.getPreco() * qtd)
            print(f"{n} =  {produto.getNome()} valor = R${produto.getPreco():.2f} valor total {produto.getPreco() * qtd}")
            print(f"Preco total da compra {valor_total}")
            n+=1
