import urllib.request
import json

cep = input("Digite o CEP: ").replace("-", "").strip()
url = f"https://viacep.com.br/ws/{cep}/json/"

try:
    with urllib.request.urlopen(url) as resposta:
        dados = json.loads(resposta.read().decode())

        if "erro" in dados:
            print("CEP não encontrado.")
        else:
            print("Logradouro:", dados["logradouro"])
            print("Bairro:", dados["bairro"])
            print("Cidade:", dados["localidade"])
            print("Estado:", dados["uf"])

except:
    print("Falha ao consultar o CEP.")
