valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

print("Valor em reais: R$", valor_reais)
print("Valor em dólares: US$", round(valor_dolar, 2))
print("Valor em euros: €", round(valor_euro, 2))