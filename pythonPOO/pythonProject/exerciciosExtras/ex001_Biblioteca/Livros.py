class Livros():
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__estadoLivro = True

    def getTitulo(self):
        return f"{self.__titulo}"
    def setTitulo(self, titulo):
        self.__titulo = titulo
    def getAutor(self):
        return self.__autor
    def setAutor(self, autor):
        self.__autor = autor

    def getEstado(self):
        return self.__estadoLivro

    def emprestar(self):
        if(self.getEstado() == False):
            print(f"Livro {self.getTitulo()} está emprestado")
        else:
            self.__estadoLivro = False
            print(f"Livro {self.getTitulo()} foi emprestado com sucesso")
