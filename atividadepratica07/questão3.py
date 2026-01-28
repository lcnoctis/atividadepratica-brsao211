nome_arquivo = input("Digite o nome do arquivo: ")

try:
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            print(linha.rstrip())
except FileNotFoundError:
    print("Erro: arquivo não encontrado.")
except:
    print("Erro ao abrir o arquivo.")
