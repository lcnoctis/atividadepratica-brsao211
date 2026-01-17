temperatura = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C, F, K): ").upper()
destino = input("Unidade de destino (C, F, K): ").upper()

if origem == "C":
    if destino == "F":
        resultado = temperatura * 9 / 5 + 32
    elif destino == "K":
        resultado = temperatura + 273.15
    else:
        resultado = temperatura

elif origem == "F":
    if destino == "C":
        resultado = (temperatura - 32) * 5 / 9
    elif destino == "K":
        resultado = (temperatura - 32) * 5 / 9 + 273.15
    else:
        resultado = temperatura

elif origem == "K":
    if destino == "C":
        resultado = temperatura - 273.15
    elif destino == "F":
        resultado = (temperatura - 273.15) * 9 / 5 + 32
    else:
        resultado = temperatura

print("Resultado:", round(resultado, 2), destino)
