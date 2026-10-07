from Livros import Livros
from Biblioteca import Biblioteca


def main():
    l1 = Livros("RitaLee Uma auto biografia", "RitaLee")
    b1 = Biblioteca()
    b1.addLivros(l1)
    b1.mostrarColecao()
    l2 = Livros("Ayrton Senna - Heroi revelado", "Ernesto Rodrigues")
    b1.addLivros(l2)
    b1.mostrarColecao()
    l1.emprestar()
    l2.emprestar()

if __name__ == "__main__":
    main()