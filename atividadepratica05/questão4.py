from datetime import date

ano = int(input("Digite o ano de nascimento: "))
mes = int(input("Digite o mês de nascimento: "))
dia = int(input("Digite o dia de nascimento: "))

data_nascimento = date(ano, mes, dia)
data_atual = date.today()

dias_vivo = (data_atual - data_nascimento).days

print("Você está vivo há", dias_vivo, "dias")