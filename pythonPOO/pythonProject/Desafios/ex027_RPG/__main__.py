from Classes import Guerreiro, Mago

def main():
    g1 = Guerreiro("Link")
    m1 = Mago("Zelda")
    op = 1

    while op != 10:
        if op % 2 == 1:
            print("---VEZ DO JOGADOR 1---")
            g1.atacar(m1)
        else:
            print("---VEZ DO JOGADOR 2---")
            m1.atacar(g1)

        op += 1



if __name__ == "__main__":
    main()