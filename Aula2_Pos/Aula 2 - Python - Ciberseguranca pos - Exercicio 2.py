# Fazer um programa que leia 5 números inteiros
# Calcule a média entre eles
# E mostre quantos são maiores do que a média

# 1. Ler a média
# 1.1 Calcular a soma
# 2. Calcular a média
# 3. Calcular quantos são maiores

numeros = []
soma = 0

for i in range (5):
    numero = int(input("Digite um número: "))
    soma += numero
    numeros.append(numero)

media = soma / 5
print("Média: ", media)

qtde = 0
for numero in numeros:
    if numero > media:
        qtde += 1
print("Quantidade de números acima da média é de ",qtde)

print("========================================================")

# Ler uma quantidade de números positivos
# A leitura termina quando um número negativo for digitado
# E mostre quais números são maiores que a média

numeros = []
soma = 0
qtde = 0

while True:
    numero = int(input("Digite um número: "))
    if numero < 0:
        break
    qtde += 1
    soma += numero
    numeros.append(numero)

media = soma / qtde
print("Média: ", media)

print("Os numeros maiores que a média são")
for numero in numeros:
    if numero > media:
        print(numero)


