from Classes import Horista, Mensalista


def main():
    mensalista = Mensalista("Amanda", 9500)
    mensalista.calc_salario()
    horista = Horista("Paulo", 12, 200)
    horista.calc_salario()


if __name__ == "__main__":
    main()