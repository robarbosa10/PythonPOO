#from Produto import Produto


class Carrinho:
    def __init__(self):
        self.__produto = []

    def addCarrinho(self, produto, qtd):
        produto.retirar_estoque(qtd)
        self.__produto.append(produto)
        print(f"{produto.getNome()} - Preco de venda: R$ {produto.getPreco():.2f} - estoque {produto.getEstoque()}")



    def resumo(self):
        valor_total = 0
        print("--CARRINHO TOTAL--")
        for prod in self.__produto:
            print(f"{prod.getNome()} x {prod.getAddCarrinho()} = R${prod.getPreco() * prod.getAddCarrinho():.2f}")
            valor_total = valor_total + (prod.getAddCarrinho() * prod.getPreco())
        print(f"VALOR TOTAL = R${valor_total:.2f}")