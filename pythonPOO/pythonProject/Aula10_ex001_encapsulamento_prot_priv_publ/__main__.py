from ex002_banco import ContaBancario


def main():
    conta1 = ContaBancario("Rogerio", 12, 1500.15)

    conta1.deposito(2000)
    conta1.saque(3600)
    conta1.saque(350)
    conta1.saque(3150)
    print(conta1)
    conta1._ContaBancario__valorConta = 0 #teste
    print(conta1.__dict__)
    print(conta1)
if __name__ == "__main__":
    main()