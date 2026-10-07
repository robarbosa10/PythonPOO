class Biblioteca:
    def __init__(self):
        self.__livros = []

    def addLivros(self, livro):
        self.__livros.append(livro)
        print(f"Livro = {livro.getTitulo()} do autor {livro.getAutor()} foi cadastrado com sucesso.")

    def mostrarColecao(self):
        for livro in self.__livros:
            print(f"Livro = {livro.getTitulo()}")
