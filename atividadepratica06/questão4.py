import urllib.request
import json

moeda = input("Digite o código da moeda (ex: USD, EUR): ").upper()
url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

try:
    with urllib.request.urlopen(url) as resposta:
        dados = json.loads(resposta.read().decode())
        chave = f"{moeda}BRL"

        if chave not in dados:
            print("Moeda não encontrada.")
        else:
            info = dados[chave]
            print("Moeda:", moeda)
            print("Valor atual:", info["bid"])
            print("Máxima:", info["high"])
            print("Mínima:", info["low"])
            print("Última atualização:", info["create_date"])

except:
    print("Erro ao consultar a cotação.")
