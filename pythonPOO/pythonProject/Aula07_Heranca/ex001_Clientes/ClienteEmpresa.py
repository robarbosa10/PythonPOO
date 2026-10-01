
from Clientes import Cliente

class ClienteEmpresa(Cliente):
    def __init__(self,nome, telefone, email, cnpj, razaoSocial):
        super().__init__(nome, telefone, email)
        self.cnpj = cnpj
        self.razaoSocial = razaoSocial

    def mostrar_dados(self):
        print("=== CLIENTE EMPRESA ===")
        print(f"Nome = {self.nome}\nEmail = {self.email}\nTelefone = {self.telefone}\nCNPJ = {self.cnpj}\nRazao Social = {self.razaoSocial}")