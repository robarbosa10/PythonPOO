from Produto import Produto
from Carrinho import Carrinho

def main():
    c1 = Carrinho()
    p1 = Produto("Teclado", 59.90, 10)
    p2 = Produto("Celular Iphone", 3500, 5)
    c1.addCarrinho(p1, 3)
    c1.addCarrinho(p2, 2)





if __name__ ==  "__main__":
    main()