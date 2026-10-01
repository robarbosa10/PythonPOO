class ContaBancario:
    """
    Cria uma conta e permite fazer saques e depositos
    """
    def __init__(self, nome, conta, valorConta = 0.0):
        self.nome = nome
        self.conta = conta
        self.valorConta = valorConta

    def deposito(self, valorDeposito):
        self.valorConta = self.valorConta + valorDeposito
        print(f"Voce depositou R$ {valorDeposito:.2f} e agora tem {self.valorConta}")
    def saque(self, valorSaque):
        if(valorSaque > self.valorConta):
            print(f"Erro, voce tem o total de {self.valorConta}")
        else:
            self.valorConta = self.valorConta - valorSaque
            print(f"Saque no valor de {valorSaque:.2f} efetuado com sucesso, agora voce tem o valor de {self.valorConta:.2f}")


    def __str__(self):
        return f"Titular da conta: {self.nome} conta: {self.conta} tem o total de R$ {self.valorConta:.2f}"



conta1 = ContaBancario("Rogerio", 12, 1500.15)

conta1.deposito(2000)
conta1.saque(3600)
conta1.saque(350)
conta1.saque(3150)
print(conta1)
