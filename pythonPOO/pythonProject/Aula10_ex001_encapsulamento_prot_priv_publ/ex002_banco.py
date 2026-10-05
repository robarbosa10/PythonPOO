class ContaBancario:
    """
    Cria uma conta e permite fazer saques e depositos
    """
    def __init__(self, nome, conta, valorConta = 0.0):
        self._nome = nome # #protegido somente a classe mae e as classes filhas tem acesso
        self.conta = conta # +publico
        self.__valorConta = valorConta # -privado somente a classe atual tem acesso

    def deposito(self, valorDeposito):
        valorDeposito = abs(valorDeposito) #pega o valor absoluto do numero (sem - ou +)
        self.__valorConta = self.__valorConta + valorDeposito
        print(f"Voce depositou R$ {valorDeposito:.2f} e agora tem {self.__valorConta}")
    def saque(self, valorSaque):
        valorSaque = abs(valorSaque)
        if(valorSaque > self.__valorConta):
            print(f"Erro, voce tem o total de {self.__valorConta}")
        else:
            self.__valorConta = self.__valorConta - valorSaque
            print(f"Saque no valor de {valorSaque:.2f} efetuado com sucesso, agora voce tem o valor de {self.__valorConta:.2f}")


    def __str__(self):
        return f"Titular da conta: {self._nome} conta: {self.conta} tem o total de R$ {self.__valorConta:.2f}"



