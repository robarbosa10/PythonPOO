from Classes import Aluno, Professor, Funcionario

def main():
    a1 = Aluno("Rogerio", 12, "TI", "TI1A")
    p1 = Professor("Cleverton", 33, "Redes", "Senior")
    f1 = Funcionario("Leliane", 45, "Secretaria", "adm")

    a1.fazerAniversario()
    p1.fazerAniversario()
    f1.fazerAniversario()
    a1.fazerMatricula()
    f1.estudar()
    p1.estudar()

if __name__ == "__main__":
    main()
