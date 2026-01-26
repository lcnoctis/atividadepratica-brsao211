def eh_palindromo(texto):
    texto_limpo = "".join(letra.lower() for letra in texto if letra.isalnum())
    return texto_limpo == texto_limpo[::-1]

texto = input("Digite uma palavra ou frase: ")

resultado = eh_palindromo(texto)

if resultado:
    print("Sim")
else:
    print("Não")
