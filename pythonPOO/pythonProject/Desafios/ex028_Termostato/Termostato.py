class Termostato():
    def __init__(self):
        self.__temperatura = 24

    @property
    def temperatura(self):
        return f"{self.__temperatura} GRAUS CELCIUS"


    def SetTemperatura(self, valor):
        if 16 >= valor <= 30:
            self.__temperatura = valor
            print(f"temperatura {self.__temperatura}")
        else:
            print("Erro")