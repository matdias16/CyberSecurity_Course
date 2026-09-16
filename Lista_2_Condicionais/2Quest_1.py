# Tendo como dados de entrada a altura e o sexo de uma pessoa, implemente um
# programa que calcule seu peso ideal, utilizando as seguintes fórmulas:
# • para homens: (72.7 * h) – 58;
# • para mulheres: (62.1 * h) – 44.7.

altura = float(input("Digite a altura da pessoa: "))
sexo = input("Digite o sexo da pessoa (M/F): ")
if sexo == "M":
    Peso_ideal_M = (72.7 * altura) - 58
    print(f"O peso ideal para uma pessoa do sexo masculino e altura {altura} m é {Peso_ideal_M:.2f} Kg")
elif sexo == "F":
    Peso_ideal_F = (62.1 * altura) - 44.7
    print(f"O peso ideal para uma pessoa do sexo feminino e altura {altura} m é {Peso_ideal_F:.2f} Kg")
else:
    print("Sexo inválido, digite M para masculino ou F para feminino")
