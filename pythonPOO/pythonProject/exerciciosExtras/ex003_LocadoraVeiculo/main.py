from Veiculo import Carro, Moto



class main():
    carro1 = Carro("ONIX", "ABC-123", 150, 4)
    moto1 = Moto("CB 500", "CBA-321", 90, 500)
    carro1.informacoes()
    carro1.calcular_valor(3)
    moto1.informacoes()
    moto1.calcular_valor(2)



if __name__ == "__main__":
    main()