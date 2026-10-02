from Classes import Guerreiro, Mago

def main():
    g1 = Guerreiro("Link", 5000, "ok")
    m1 = Mago("zelda", 5000, "asd")

    print(g1.__dict__)
    print(m1.__dict__)
    print(m1)



if __name__ == "__main__":
    main()