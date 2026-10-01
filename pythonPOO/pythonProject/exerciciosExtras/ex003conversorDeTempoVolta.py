voltaTotal = float(input("Qual a volta? "))
print("Volta total em segundos: ", voltaTotal)



if(int(voltaTotal) > 60 and int(voltaTotal) < 120):
    conversor = voltaTotal - 60
    minutos = 1
    segundos = int(conversor)
    mile = conversor - int(conversor)
    print(f"{int(minutos)} Minutos e {segundos:.0f} Segundos e {mile:.3f} Milesimos ")
elif(voltaTotal > 120):
    minutos = int(voltaTotal) / 60
    conversor = voltaTotal - (int(minutos) * 60)
    segundos = conversor
    mile = conversor - int(conversor)
    print(f"{int(minutos)} Minutos e {segundos:.0f} Segundos e {mile:.3f} Milesimos ")
