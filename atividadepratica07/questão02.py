import csv

def escrever_csv(nomearquivo,dados):
    try: 
        with open(nomearquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(['Nome', 'Idade', 'Cidade'])
            for linha in dados:
                escritor.writerow(linha)
        return "Arquivo CSV criado com sucesso." 
    except Exception as e:
        return f"Erro ao criar o arquivo CSV: {e}"

dados = [
    ['Ana', 28, 'São Paulo'],   
    ['Bruno', 34, 'Rio de Janeiro'], 
    ['Carla', 25, 'Belo Horizonte']    
]

nomearquivo = input("Digite o nome do arquivo CSV a ser criado: ")
print(escrever_csv(nomearquivo, dados))