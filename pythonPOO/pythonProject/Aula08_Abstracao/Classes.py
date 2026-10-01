from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazerAniversario(self):
        self.idade += 1
        print(f"Parabens {self.nome}, acabou de fazer aniversario. {self.idade}")

    @abstractmethod
    def estudar(self):
        pass

class Aluno(Pessoa):
    def __init__(self,nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazerMatricula(self):
        print(f"{self.nome} Acabou de fazer uma matricula")

    def estudar(self):
        print(f"Esta estudando na sala {self.turma} no curso {self.curso}")


class Professor(Pessoa):
    def __init__(self,nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def darAula(self):
        pass

    def estudar(self):
        print(f"{self.nome} é um especialista em {self.especialidade} no nivel {self.nivel}")


class Funcionario(Pessoa):
    def __init__(self,nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def baterPonto(self):
        pass

    def estudar(self):
        print(f"{self.nome} quem tem o cargo de: {self.cargo} no setor {self.setor}")





