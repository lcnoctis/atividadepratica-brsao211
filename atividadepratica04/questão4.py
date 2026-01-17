pares = 0
impares = 0

quantidade = int(input("Quantos números deseja digitar? "))

for i in range(quantidade):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Quantidade de pares:", pares)
print("Quantidade de ímpares:", impares)
