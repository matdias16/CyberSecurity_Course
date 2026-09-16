# Peça 5 números ao usuário. Fazendo uso de laços, organize e mostre eles em ordem crescente.

numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

for i in range(len(numeros)): #qtd de elementos na lista e em seguida i ao i 5
    for j in range(len(numeros) - 1):
        if numeros[j] > numeros[j + 1]:
            temp = numeros[j]
            numeros[j] = numeros[j + 1]
            numeros[j + 1] = temp

print("Números em ordem crescente:")
for numero in numeros:
    print(numero)