from Cafeteira import Cafe, Leite, Cha

def main():
    cafe = Cafe()
    leite = Leite()
    cha = Cha()
    cafe.preparar()
    leite.preparar()
    cha.preparar()


if __name__ == "__main__":
    main()