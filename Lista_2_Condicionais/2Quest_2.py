# O IMC – Índice de Massa Corporal é um critério da Organização Mundial de Saúde para dar uma indicação sobre a condição de peso de uma pessoa adulta. 
# A fórmula é IMC = peso / altura2. 
# Implemente um programa que leia o peso e a altura de um adulto e mostre sua condição de acordo com a tabela abaixo.
# IMC em adultos Condição
# • Abaixo de 18,5 – Abaixo do peso
# • Entre 18,5 e 25 – Peso normal
# • Entre 25 e 30 – Acima do peso
# • Acima de 30 – Obeso


print("IMC – Índice de Massa Corporal")
print("---------------------------------------")
altura = float(input("Digite a altura da pessoa: "))
peso = float(input("Digite o peso da pessoa: "))
imc = peso / altura**2
if imc < 18.5:
    print(f"A pessoa está com um imc de {imc:.2f}, considerada Abaixo do peso")
elif imc > 18.5 and imc < 25:
    print(f"A pessoa está com um imc de {imc:.2f}, considerada Peso normal")
elif imc > 25 and imc < 30:
    print(f"A pessoa está com um imc de {imc:.2f}, considerada Acima do peso")
elif imc > 30:
    print(f"A pessoa está com um imc de {imc:.2f}, considerada Obeso")
