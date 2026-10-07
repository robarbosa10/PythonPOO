from Avaliacao import Avaliacao


def main():
    aluno1 = Avaliacao("Felipe", "POO")
    print(aluno1.getNota())
    aluno1.setNota(7)
    print(aluno1.getNota())


if __name__ == "__main__":
    main()