from Classes import Moto, Caminhao, Drone

def main():
    entregaDrone = Drone(8)
    entregaCaminhao = Caminhao(50)
    entregaMoto = Moto(90)
    entregaDrone.calcular_frete()
    entregaMoto.calcular_frete()
    entregaCaminhao.calcular_frete()

if __name__ == "__main__":
    main()