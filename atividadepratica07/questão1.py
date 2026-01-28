import pandas as pd

def processar_logs_treinamento(arquivolog):
    try: 
        leitor = pd.read_csv(arquivolog)
        media = leitor['tempo_execução'].mean()
        desvio_padrao = leitor['tempo_execução'].std()
        return f"Media: {media:.2f}, Desvio Padrão: {desvio_padrao:.2f}"
    
    except FileNotFoundError: 
        return "Erro ao processar o arquivo de log."

arquivo = input("Digite o nome do arquivo de log de treinamento: ")
print(processar_logs_treinamento(arquivo))