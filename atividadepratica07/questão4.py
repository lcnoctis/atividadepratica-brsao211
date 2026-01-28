import json

arquivo = "dados.json"

try:
    dados = {
        "nome": input("Digite o nome: "),
        "idade": int(input("Digite a idade: ")),
        "cidade": input("Digite a cidade: ")
    }

    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

    with open(arquivo, "r", encoding="utf-8") as f:
        dados_lidos = json.load(f)

    print("Nome:", dados_lidos["nome"])
    print("Idade:", dados_lidos["idade"])
    print("Cidade:", dados_lidos["cidade"])

except:
    print("Falha ao salvar ou ler o arquivo JSON.")
