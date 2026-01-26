preco = float(input("Digite o preço do produto: R$ "))
desconto = float(input("Digite a porcentagem de desconto: "))

valor_desconto = preco * (desconto / 100)
preco_final = preco - valor_desconto

print("Valor do desconto: R$", round(valor_desconto, 2))
print("Preço final: R$", round(preco_final, 2))
