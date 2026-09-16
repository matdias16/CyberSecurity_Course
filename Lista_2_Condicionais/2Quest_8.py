# Implemente um programa que solicite uma data com hora, pedindo em separado: 
# dia, mês, ano, hora, minuto e segundo. 
# Pergunte ao usuário que informação ele deseja acrescentar, e em qual quantidade. 
# Informar a nova data de acordo com o solicitado pelo usuário.
# Ex.: Informada a data 31/12/2001 23:59:59, se o usuário pedir para acrescentar um segundo a data deve ser exibida como 01/01/2002 00:00:00.
# Para determinar se um ano é bissexto, execute estas etapas:
# 1. Se o ano for uniformemente divisível por 4, vá para a etapa 2. Caso contrário, vá para a etapa 5.
# 2. Se o ano for uniformemente divisível por 100, vá para a etapa 3. Caso contrário, vá para a etapa 4.
# 3. Se o ano for uniformemente divisível por 400, vá para a etapa 4. Caso contrário, vá para a etapa 5.
# 4. O ano é bissexto (tem 366 dias).
# 5. O ano não é um ano bissexto (tem 365 dias).

Dia = int(input("Digite um dia: "))
Mes = int(input("Digite um mes: "))
Ano = int(input("Digite um ano (Com 4 dígitos): "))
Hora  = int(input("Digite as horas: "))
Minuto  = int(input("Digite os minutos: "))
Segundo = int(input("Digite os segundos: "))
print(f"{Dia:02d}/{Mes:02d}/{Ano} - {Hora:02d}:{Minuto:02d}:{Segundo:02d}")

Acrescentar_Tipo = input("Qual informação deseja acrescentar ? (Hora, Minuto ou Segundo): ")
Acrescentar_Valor = int(input("Quanto deseja acrescentar? "))

if Ano % 4 == 0:
    if Ano % 100 == 0:
        if Ano % 400 == 0:
            bissexto = True
        else:
            bissexto = False
    else:
        bissexto = True
else:
    bissexto = False
    
def dias_mes(mes, bissexto):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        return 29 if bissexto else 28
    
if Acrescentar_Tipo == "Segundo":
    Segundo = Segundo + Acrescentar_Valor

elif Acrescentar_Tipo == "Minuto":
    Minuto = Minuto + Acrescentar_Valor

elif Acrescentar_Tipo == "Hora":
    Hora = Hora + Acrescentar_Valor

else:
    print("Tipo inválido")

Minuto += Segundo // 60
Segundo = Segundo % 60

Hora += Minuto // 60
Minuto = Minuto % 60

Dia += Hora // 24
Hora = Hora % 24

while True:
    limite = dias_mes(Mes, bissexto)

    if Dia <= limite:
        break

    Dia = Dia - limite
    Mes = Mes + 1

    if Mes > 12:
        Mes = 1
        Ano = Ano + 1

        if Ano % 4 == 0:
            if Ano % 100 == 0:
                if Ano % 400 == 0:
                    bissexto = True
                else:
                    bissexto = False
            else:
                bissexto = True
        else:
            bissexto = False

print(f"Nova data: {Dia:02d}/{Mes:02d}/{Ano} {Hora:02d}:{Minuto:02d}:{Segundo:02d}")