class Avaliacao():
    def __init__(self, nome, disciplina):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = 0

    def setNota(self, nota):
        if 0 <= nota <= 10:
            self._nota = nota
        else:
            print("nota invalida")

    def getNota(self):
        return self._nota