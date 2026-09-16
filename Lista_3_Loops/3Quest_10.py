# Solicitar ao usuário duas datas e calcular a quantidade de dias entre elas (levar em consideração os anos bissextos)

Dia1 = int(input("Digite um dia: "))
Mes1 = int(input("Digite um mes: "))
Ano1 = int(input("Digite um ano (Com 4 dígitos): "))
Dia2 = int(input("Digite um dia: "))
Mes2 = int(input("Digite um mes: "))
Ano2 = int(input("Digite um ano (Com 4 dígitos): "))

def bissexto(ano):
    return (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)

def dias_ate_data(dia, mes, ano):
    meses = [31, 28, 31, 30, 31, 30,
             31, 31, 30, 31, 30, 31]

    total = dia 

    # Soma os meses anteriores
    for i in range(mes - 1):
        total = total + meses[i] 

    if mes > 2 and bissexto(ano):
        total = total + 1 

    total += ano * 365                     

    total += ano // 4 - ano // 100 + ano // 400

    return total

data1 = dias_ate_data(Dia1, Mes1, Ano1)
data2 = dias_ate_data(Dia2, Mes2, Ano2)

diferenca = abs(data2 - data1)
print("Quantidade de dias entre as datas é:", diferenca)