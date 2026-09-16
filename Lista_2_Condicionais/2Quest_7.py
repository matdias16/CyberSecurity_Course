# Implemente um programa que solicite o dia, mês e ano (com 4 dígitos) de nascimento
# de uma pessoa, e pergunte em qual formato deve exibir a data, como segue:
# Código de Exibição de Data
# • 1 – Data simples. Ex.: 10/08/1990;
# • 2 – Data abreviada. Ex.: 10/ago/1990;
# • 3 – Data completa. Ex.: 10 de agosto de 1990.

Meses_Abrev = ["","Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
Meses_Inteiro = ["","Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

Dia = int(input("Digite o dia do seu nascimento: "))
Mes = int(input("Digite o mes do seu nascimento: "))
Ano = int(input("Digite o ano do seu nascimento (Com 4 dígitos): "))
Exibição = int(input(
    "Digite o número da exibição:\n"
    "1 – Data simples. Ex.: 10/08/1990\n"
    "2 – Data abreviada. Ex.: 10/ago/1990\n"
    "3 – Data completa. Ex.: 10 de agosto de 1990\n"
    ))
if Exibição == 1:
    print(f"{Dia:02d}/{Mes:02d}/{Ano}")
elif Exibição == 2:
    print(f"{Dia:02d}/{Meses_Abrev[Mes]}/{Ano}")
elif Exibição ==3:
    print(f"{Dia:02d} de {Meses_Inteiro[Mes]} de {Ano}")
else:
    print("Opção de exibição inválida")

