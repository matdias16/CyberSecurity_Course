# Elaborar um programa que receba um número em binário, e mostre o seu valor em decimal.

Binario_Decimal = 0
Binario = input("Digite um número binário: ")
for numero in Binario:
    Binario_Decimal = Binario_Decimal*2 + int(numero)
print(f"O valor decimal do binário {Binario} em decimal é", Binario_Decimal)