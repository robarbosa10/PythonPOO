class Livro():
    def __init__(self, titulo, nmrPaginas, pagAtual = 1):
        self.titulo = titulo
        self.nmrPaginas = nmrPaginas
        self.pagAtual = pagAtual

    def avancarPaginas(self, avancarPagina):
        #print(f"pagina atual {self.pagAtual}")
        if(avancarPagina <= self.nmrPaginas):
            for pag in range(avancarPagina):
                print(f"pag = {self.pagAtual}")
                self.pagAtual += 1
                if(self.pagAtual == self.nmrPaginas):
                    break
    def __str__(self):
        print(f"Pagina Atual = {self.pagAtual}")

l1 = Livro("Ok", 20)

l1.avancarPaginas(5)
l1
l1.avancarPaginas(20)
