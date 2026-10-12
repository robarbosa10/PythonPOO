from Funcionario import Atendente, Supervisor


class main():
    f1 = Atendente("Rogerio", 2000, 150)
    lider = Supervisor("Larissa", 2000, 200, "Alfa")
    f1.calcular_salario()
    lider.calcular_salario()

if __name__ == "__main__":
    main()