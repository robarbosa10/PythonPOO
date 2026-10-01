class Funcionario():
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def __str__(self):
        return f"Funcionario: {self.nome} setor: {self.setor} tem o cargo: {self.cargo}"
    def apresentacao(self):
        print(f"Ola, sou {self.nome}, sou {self.cargo} no setor {self.setor}")


fun1 = Funcionario("Cassiane", "Comercial", "Vendedor Interna")

fun1.apresentacao()
