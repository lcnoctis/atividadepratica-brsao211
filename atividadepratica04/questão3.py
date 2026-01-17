senha = input("Digite uma senha: ")

tem_numero = False

for caractere in senha:
    if caractere.isdigit():
        tem_numero = True

if len(senha) >= 8 and tem_numero:
    print("Senha válida")
else:
    print("Senha inválida")
